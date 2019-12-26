from django.db import models

# Create your models here.

class MC_Answer(models.Model):
    text = models.CharField(max_length=255)
    letter = models.CharField(max_length=1)

class Question(models.Model):
    text = models.CharField(max_length=511)
    multiple_choice = models.BooleanField()
    lettered_parts = models.BooleanField()
    mc_answers = models.ManyToManyField(MC_Answer)
    mc_correct = models.ForeignKey(MC_Answer, models.SET_NULL, blank=True, null=True, related_name="mc_answers")
