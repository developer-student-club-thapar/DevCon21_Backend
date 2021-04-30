from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.forms import ParticipantForm
from api.models import Participant


@csrf_exempt
def participantForm(request):
    if request.method == "POST":

        data = {
            "firstName": request.POST["firstName"],
            "lastName": request.POST["lastName"],
            "institution": request.POST["institution"],
            "email": request.POST["email"],
            "yos_designation": request.POST["yos_designation"],
            "mobile": request.POST["mobile"],
            "referralCode": request.POST["referralCode"],
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
            return HttpResponse("Success")

        return HttpResponse("Bad form data", status=403)

    return HttpResponse("Only POST request allowed duhh.", status=403)
