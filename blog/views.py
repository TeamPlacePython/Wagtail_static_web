from django.shortcuts import redirect
from django.views import View
from django.contrib import messages

from .models import BlogSubscriber


class SubscribeView(View):
    def post(self, request):
        if email := request.POST.get("email"):
            # Vérifier si l'email existe déjà
            if not BlogSubscriber.objects.filter(email=email).exists():
                BlogSubscriber.objects.create(email=email)
                messages.success(request, "Merci pour votre inscription !")
            else:
                messages.info(request, "Vous êtes déjà inscrit.")
        else:
            messages.error(
                request, "Veuillez entrer une adresse email valide."
            )

        return redirect(request.META.get("HTTP_REFERER", "/"))
