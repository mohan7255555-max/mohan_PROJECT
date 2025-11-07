
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    tech_stack = models.CharField(max_length=300)

    def _str_(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.name