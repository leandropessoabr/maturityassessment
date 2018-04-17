from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import FormView
from .models import Assessment, AssessmentAnswer, Dimension, Criteria
from django import forms
from django.urls import reverse

class MainPageView(generic.ListView):
    template_name = 'maturity/index.html'
    def get_queryset(self):
        return Dimension.objects.all()

class AssessmentListView(generic.ListView):
    template_name = 'maturity/assessment_list.html'
    def get_queryset(self):
        return Assessment.objects.all()

class AnswerListView(generic.DetailView):
    model = Assessment
    template_name = 'maturity/answer_list.html'

class NewAssessmentForm(forms.Form):
    name = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField(label='User email', max_length=100)

class NewAssessmentView(FormView):
    template_name = "maturity/new_assessment.html"
    form_class = NewAssessmentForm
    sucess_url = 'maturity/assessment_list.html'

def set_new_assessment_data(request):
    if request.method == 'POST':
        form = NewAssessmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name)
            print(email)
            Assessment.createAssessment(name, email)
    else:
        form = NameForm()

    return HttpResponseRedirect(reverse('maturity:assessments'))









