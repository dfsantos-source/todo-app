from django.db import models

# Create your models here.
class TodoItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(max_length=200, null=True, blank=True)
    time = models.TimeField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name