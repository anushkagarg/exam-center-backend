from django.contrib import admin
from .models import Quiz, Question, Submission, ScheduledQuiz
from .forms import SubmissionForm


class SubmissionAdmin(admin.ModelAdmin):
    form = SubmissionForm

admin.site.register(Quiz)
admin.site.register(ScheduledQuiz)
admin.site.register(Question)
admin.site.register(Submission, SubmissionAdmin)