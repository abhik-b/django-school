from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Assignment, Question, Choice
from django.views.generic import DetailView
from django.db.models import Q
from classs.models import Classs
# Create your views here.


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = "assignment_detail.html"
    context_object_name = 'a'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ass = Assignment.objects.get(id=question.assignment.id)
    return render(request, 'results.html', {'question': question, 'assignment': ass})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ass = Assignment.objects.get(id=question.assignment.id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ass.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice.choice_text == question.answer_text:
            print('right ans')
            ass.marks += 1
            ass.save()
        else:
            print('wrong ans')
            ass.marks = 0
            ass.save()
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

    return HttpResponseRedirect(reverse('assignments:results', args=(question.id,)))


def search(request, class_id):
    assignments = Assignment.objects.all()
    clas = Classs.objects.get(id=class_id)
    query = request.GET.get('q')
    if query:
        ass = assignments.filter(
            Q(id__icontains=query) | Q(subject__icontains=query)
        ).distinct()

    # floor = Floor.objects.filter(flname__startswith=query)
    context = {
        "ass": ass,
        'class': clas
        # 'floor': floor
    }
    return render(request, "assignments-searchresults.html", context)
