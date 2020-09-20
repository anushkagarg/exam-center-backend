from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

User = get_user_model()


class Quiz(models.Model):
    name=models.CharField(max_length=40)
    organization=models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'O'}, related_name='all_quiz')
    staff=models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'T'}, related_name='quiz')
    is_private=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def questions(self):
        return self.question_set.all()


class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    name=models.TextField()
    options=ArrayField(models.TextField())
    answer=ArrayField(models.CharField(max_length=1))
    is_choice=models.BooleanField(default=True)
    is_multiple_choice=models.BooleanField(default=False)
    tags=ArrayField(models.CharField(max_length=40))

    def __str__(self):
        return self.name


class ScheduledQuiz(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    staff=models.ManyToManyField(User)
    students=models.ManyToManyField(User, related_name='assigned_quiz')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return self.quiz.name



class Submission(models.Model):
    quiz=models.ForeignKey(ScheduledQuiz, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'S'})
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(null=True, blank=True)
    answers=ArrayField(ArrayField(models.TextField()), null=True, blank=True)

  
    def __str__(self):
        return self.user.username + ' - ' + self.quiz.quiz.name

    def save(self, *args, **kwargs):
        if self.pk:
            self.end_time = timezone.now()
            max_length = len(max(self.answers, key=lambda i: len(i)))
            self.answers = list(map(lambda x: x + [None]*(max_length - len(x)), self.answers))
        super().save(*args, **kwargs)