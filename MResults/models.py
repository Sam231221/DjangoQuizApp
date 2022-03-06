import imp
from django.db import models
from MQuiz.models import Quiz
from django.contrib.auth.models import User
# Create your models here.
class Result(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.FloatField()
    