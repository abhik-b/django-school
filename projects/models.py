from django.db import models
from tinymce import HTMLField
from classs.models import Classs
# Create your models here.


class Project(models.Model):
    project_title = models.CharField(max_length=120)
    subject = models.CharField(max_length=250)

    attachment = models.FileField(blank=True, null=True)
    class_name = models.ForeignKey(Classs, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title
