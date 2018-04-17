from django.db import models
from django.utils import timezone

# Create your models here.

class Dimension(models.Model):
    dimension_name = models.CharField(max_length=64)
    dimension_description = models.CharField(max_length=500)

    def __str__(self):
        return self.dimension_name + ' (' + str(self.pk) + ')'

class Criteria(models.Model):
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    criteria_name = models.CharField(max_length=64)
    criteria_description = models.CharField(max_length=500)

    def __str__(self):
        return self.criteria_name

class Assessment(models.Model):
    assessment_date = models.DateTimeField()
    user_name = models.CharField(max_length=120)
    user_email = models.CharField(max_length=120)

    def __str__(self):
        return 'Assessment of ' + self.user_email + ' (' + str(self.pk) + ')'

    def create_answers(self):
        criteria_list = Criteria.objects.all()
        for crit in criteria_list:
            answer = AssessmentAnswer.objects.create(assessment=self, criteria=crit, value=-1)

    def field_list_view(self):
        return [self.user_email, self.user_name, str(self.assessment_date)]

    @staticmethod
    def createAssessment(name, email):
        ass = Assessment.objects.create(user_name=name, user_email=email, assessment_date=timezone.now())
        ass.create_answers()

class AssessmentAnswer(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return self.get_dimension_name() + ' | ' + self.get_criteria_name() + ' | ' + self.get_assessment_name()

    def get_dimension_name(self):
        return str(self.criteria.dimension)

    def get_criteria_name(self):
        return str(self.criteria)

    def get_assessment_name(self):
        return str(self.assessment)

