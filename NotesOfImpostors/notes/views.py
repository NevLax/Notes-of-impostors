from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Notes


def getnotes(request):
    notes = Notes.objects.all()
    context = {
        "notes": notes,
    }
    template = loader.get_template("prenote.html")
    return HttpResponse(template.render(context, request))


@login_required
def getnote(request, k):
    template = loader.get_template("note.html")
    note = Notes.objects.get(pk=k)
    context = {
        "note": note,
    }
    return HttpResponse(template.render(context, request))
