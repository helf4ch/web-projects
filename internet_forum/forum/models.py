from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    theme = models.CharField(max_length=120)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.theme


class Post(models.Model):
    post_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        end = ""
        if len(self.post_text) > 120:
            end = "..."
        return self.post_text[:120] + end