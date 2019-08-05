from django.db import models
import datetime as dt

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length =60)
    project_details = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='images/', blank=True)
    project_link = models.CharField(max_length =60)

    @classmethod
    def todays_project(cls):
        projecthub = cls.objects.filter()
        return projecthub

    @classmethod
    def days_project(cls,date):
        projecthub = cls.objects.filter()
        return projecthub

    @classmethod
    def search_by_project_title(cls,search_term):
        projecthub = cls.objects.filter(project_title__icontains=search_term)
        return projecthub
