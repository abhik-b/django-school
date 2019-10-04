from django.shortcuts import render
from .models import Classs
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
# Create your views here.


class ClasssListView(ListView):
    model = Classs
    template_name = "index.html"
    context_object_name = 'classes'


class ClasssDetailView(DetailView):
    model = Classs
    template_name = "detail.html"
    context_object_name = 'class'


def notes(request, id):
    c = Classs.objects.get(id=id)
    notes = c.note_set.all()
    context = {
        'notes': notes, 'class': c
    }
    return render(request, 'notes.html', context)


def projects(request, id):
    c = Classs.objects.get(id=id)
    projects = c.project_set.all()
    context = {
        'projects': projects, 'class': c
    }
    return render(request, 'projects.html', context)


def assignments(request, id):
    c = Classs.objects.get(id=id)
    assignments = c.assignment_set.all()
    context = {
        'assignments': assignments, 'class': c
    }
    return render(request, 'assignments.html', context)


def attendancecheck(request, id):
    c = Classs.objects.get(id=id)
    query = int(request.GET.get('ac'))
    # total_days = 200
    # criteria = 0.75
    total_days = c.total_days
    criteria = float(c.criteria)
    if query:

        if (query/total_days) >= criteria:
            message = 'PASS'

        else:
            message = 'FAIL'
    context = {
        'message': message,
        'class': c
    }
    return render(request, 'detail.html', context)
