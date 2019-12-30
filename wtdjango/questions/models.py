from django.db import models

# Create your models here.

class QuestionManager(models.Manager):
    def create_question(self, text='', multiple_choice=False, lettered_parts=False, mc_answers=None, mc_correct=None):
        q = self.create(text=text,multiple_choice=multiple_choice,lettered_parts=lettered_parts,mc_answers=mc_answers,mc_correct=mc_correct)
        return q

class MC_AnswerManager(models.Manager):
    def creat_mc_answer(self, text='', letter=''):
        a = self.create(text=text, letter=letter)
        return a

class MC_Answer(models.Model):
    text = models.CharField(max_length=255)
    letter = models.CharField(max_length=1)

class Question(models.Model):
    text = models.CharField(max_length=511)
    multiple_choice = models.BooleanField()
    lettered_parts = models.BooleanField()
    mc_answers = models.ManyToManyField(MC_Answer)
    mc_correct = models.ForeignKey(MC_Answer, models.SET_NULL, blank=True, null=True, related_name="mc_answers")
