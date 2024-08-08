from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    body=models.TextField()
    created_at=models.DateField()
    updated_at=models.DateField()

    def __str__(self):
        return self.title