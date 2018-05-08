from django.db import models
from django.db.models import Avg
from django.utils import timezone

# Create your models here.

class Dimension(models.Model):
    dimension_name = models.CharField(max_length=64)
    dimension_description = models.CharField(max_length=500)

    def __str__(self):
        return self.dimension_name
        # + ' (' + str(self.pk) + ')'

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
    current_assessment_item = models.IntegerField(default=-1)

    def __str__(self):
        return 'Assessment of ' + self.user_email + ' (' + str(self.pk) + ')'

    def create_answers(self):
        dimension_list = Dimension.objects.all()
        for dimension in dimension_list:
            DimensionResult.objects.create(assessment=self, dimension=dimension, value=-1)
        criteria_list = Criteria.objects.all()
        for crit in criteria_list:
            AssessmentAnswer.objects.create(assessment=self, criteria=crit, value=-1)

    def set_dimension_results(self):
        dimension_result_list = list(self.dimensionresult_set.all())
        for dimension_result in dimension_result_list:
            result = self.get_dimension_result(dimension_result.dimension)
            dimension_result.value = result
            dimension_result.save()
        return self.dimensionresult_set.all()

    def create_dimension_results(self):
        dimension_list = list(Dimension.objects.all())
        for dimension in dimension_list:
            result = self.get_dimension_result(dimension)
            dimension_result = DimensionResult.objects.create(assessment=self, dimension=dimension, value=result)
            dimension_result.save()
        return self.dimensionresult_set.all()

    def get_current_assessment_item(self):
        answer_list = list(self.assessmentanswer_set.all())
        if self.current_assessment_item < len(answer_list):
            answer = answer_list[self.current_assessment_item]
        else:
            self.set_dimension_results()
            answer = None
        return answer

    def get_progress_string(self):
        answer_list = list(self.assessmentanswer_set.all())
        str_return = str(self.current_assessment_item+1) + '/' + str(len(answer_list))
        return str_return


    def get_dimension_result(self, dimension):
        answers = self.assessmentanswer_set.filter(criteria__dimension__dimension_name=dimension.dimension_name)
        result = answers.aggregate(Avg('value'))
        return result.get('value__avg')

    def get_dimension_list(self):
        return Dimension.objects.all()

    def set_current_answer(self, value):
        answer = self.get_current_assessment_item()
        answer.set_value(value)
        answer.save()
        self.current_assessment_item = self.current_assessment_item + 1

    def field_list_view(self):
        return [self.user_email, self.user_name, str(self.assessment_date)]

    @staticmethod
    def createAssessment(name, email):
        ass = Assessment.objects.create(user_name=name, user_email=email, assessment_date=timezone.now(), current_assessment_item=0)
        ass.create_answers()
        return ass

class AssessmentAnswer(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return self.get_dimension_name() + ' | ' + self.get_criteria_name() + ' | ' + str(self.value)

    def set_value(self, new_value):
        self.value = new_value

    def get_dimension_name(self):
        return str(self.criteria.dimension)

    def get_criteria_name(self):
        return str(self.criteria)

    def get_criteria_description(self):
        return self.criteria.criteria_description

    def get_assessment_name(self):
        return str(self.assessment)

class DimensionResult(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return str(self.dimension) + ' | ' + str(self.value)


