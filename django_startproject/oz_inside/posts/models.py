from django.db import models
from django.contrib.auth.models import User 

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.Foreignkey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
