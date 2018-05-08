from django.urls import path

from . import views

app_name = 'maturity'
urlpatterns = [path('', views.MainPageView.as_view(), name='index'),
               path('assessments/', views.AssessmentListView.as_view(), name='assessments'),
               path('assessments/<int:pk>', views.AnswerListView.as_view(), name='answers'),
               path('assessments/answer/<int:pk>', views.AnswerView.as_view(), name='answer'),
               path('assessments/set_answer/<int:assessment_id>', views.set_answer, name='set_answer'),
               path('assessments/set/', views.set_new_assessment_data, name='set_new_assessment_data'),
               path('assessments/results/<int:pk>', views.ResultsView.as_view(), name='results')]
