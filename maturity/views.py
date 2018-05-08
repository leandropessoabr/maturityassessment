from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import FormView
from .models import Assessment, AssessmentAnswer, Dimension, Criteria
from django import forms
from django.urls import reverse

class MainPageView(generic.ListView):
    template_name = 'html5boilerplate/index.html'
    def get_queryset(self):
        return Dimension.objects.all()

class AssessmentListView(generic.ListView):
    template_name = 'maturity/assessment_list.html'
    def get_queryset(self):
        return Assessment.objects.all()

class AnswerView(generic.DetailView):
    model = Assessment
    template_name = 'html5boilerplate/criteriaanswer.html'

class AnswerListView(generic.DetailView):
    model = Assessment
    template_name = 'maturity/answer_list.html'

class ResultsView(generic.DetailView):
    model = Assessment
    template_name = 'html5boilerplate/results.html'

def set_new_assessment_data(request):
    name = request.POST['name']
    email = request.POST['email']
    ass = Assessment.createAssessment(name, email)
    return HttpResponseRedirect(reverse('maturity:answer', args=(ass.id,)))

def set_answer(request, assessment_id):
    ass = Assessment.objects.get(pk=assessment_id)
    answer = int(request.POST['value'])
    ass.set_current_answer(answer)
    ass.save()
    answer = ass.get_current_assessment_item() # gets next item
    if answer == None:
        return HttpResponseRedirect(reverse('maturity:results', args=(ass.id,)))
    else:
        return HttpResponseRedirect(reverse('maturity:answer', args=(ass.id,)))














