from pickle import TRUE
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title
