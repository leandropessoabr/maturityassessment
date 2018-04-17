from django.urls import path

from . import views

app_name = 'maturity'
urlpatterns = [path('', views.MainPageView.as_view(), name='index'),
               path('assessments/', views.AssessmentListView.as_view(), name='assessments'),
               path('assessments/<int:pk>', views.AnswerListView.as_view(), name='answers'),
               path('assessments/new/', views.NewAssessmentView.as_view(), name='new_assessment'),
               path('assessments/set/', views.set_new_assessment_data, name='set_new_assessment_data')]
