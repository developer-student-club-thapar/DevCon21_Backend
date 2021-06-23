from django.core.mail import send_mail
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.forms import ParticipantForm
from api.models import Participant

mail = """
Greetings!

Hope you are doing well.
You have been successfully registered for DevCon'21.
Devcon'21 is a series of webinars, workshops and competitions held by some great minds in the world of technology starting from 25th June 2021 to 27th June 2021.

Kindly join the discord server and Whatsapp group for further updates and connect with the community:
Discord Server: https://discord.gg/8khTrtWWBT
WhatsApp group: https://minify.live/Devcon21WhatsApp

Join us on our social media handles to know more about the event
Instagram:https://instagram.com/ieee_ncu?utm_medium=copy_link
YouTube:https://youtube.com/c/IEEENCUStudentBranch
LinkedIn:https://www.linkedin.com/company/ieee-ncu
Facebook:https://www.facebook.com/ieee.ncu/?ti=as
"""


@csrf_exempt
def participantForm(request):
    if request.method == "POST":

        data = {
            "name": request.POST["name"],
            "institution": request.POST["institution"],
            "email": request.POST["email"],
            "yos_designation": request.POST["yos_designation"],
            "mobile": request.POST["mobile"],
            "referralCode": request.POST["referralCode"].upper(),
            "event": request.POST["event"],
        }

        form = ParticipantForm(data)

        if form.is_valid():
            email = form.cleaned_data["email"]
            if Participant.objects.filter(email=email).exists():
                return HttpResponse(
                    "Participant with email already registered.", status=404
                )
            form.save()
            # TODO: Make changes below
            send_mail(
                "Devcon21 Registration Successful!",
                mail,
                "noreplydevcon@gmail.com",
                [email],
                fail_silently=False,
            )

            return HttpResponse("Success")

        return HttpResponse(
            "Please enter a valid 10 digit phone number!", status=403
        )

    return HttpResponse("Only POST request allowed duhh.", status=403)
