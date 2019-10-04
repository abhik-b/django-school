from django.shortcuts import render
from django.views.generic import DetailView
from .models import Note
from django.db.models import Q
from classs.models import Classs
# Create your views here.


class NoteDetailView(DetailView):
    model = Note
    template_name = "note-detail.html"
    context_object_name = 'note'


def search(request, class_id):
    notes = Note.objects.all()
    clas = Classs.objects.get(id=class_id)
    query = request.GET.get('q')
    if query:
        note = notes.filter(
            Q(note_title__icontains=query) | Q(subject__icontains=query)
        ).distinct()
        print(note)

    # floor = Floor.objects.filter(flname__startswith=query)
    context = {
        "note": note, 'class': clas
        # 'floor': floor
    }
    return render(request, "notes-searchresults.html", context)
