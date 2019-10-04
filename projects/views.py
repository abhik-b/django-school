from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project
from django.db.models import Q
from classs.models import Classs
# Create your views here.


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project-detail.html"
    context_object_name = 'project'


def search(request, class_id):
    projects = Project.objects.all()
    clas = Classs.objects.get(id=class_id)
    query = request.GET.get('q')
    if query:
        project = projects.filter(
            Q(project_title__icontains=query) | Q(subject__icontains=query)
        ).distinct()

    # floor = Floor.objects.filter(flname__startswith=query)
    context = {
        "project": project,
        'class': clas
        # 'floor': floor
    }
    return render(request, "projects-searchresults.html", context)
