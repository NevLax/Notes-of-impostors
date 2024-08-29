from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Notes


def getnotes(request):
    notes = Notes.objects.all()
    context = {
        "notes": notes,
    }
    template = loader.get_template("prenote.html")
    return HttpResponse(template.render(context, request))


def getnote(request, k):
    template = loader.get_template("note.html")
    note = Notes.objects.get(pk=k)
    context = {
        "note": note,
    }
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    return redirect('home')