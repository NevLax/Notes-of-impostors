from django.http import HttpResponse
from django.template import loader
from .models import Notes


def index(request):
    return HttpResponse('Hello World')


def getNotes(request):
    notes = Notes.objects.all()
    context = {
        "notes": notes,
    }
    template = loader.get_template("prenote.html")
    return HttpResponse(template.render(context, request))


def getNote(request, k):
    template = loader.get_template("note.html")

    note = Notes.objects.get(pk=k)
    context = {
        "note" : note,
    }

    return HttpResponse(template.render(context, request))