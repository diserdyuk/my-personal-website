from django.db import models
from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

