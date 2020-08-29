from django.db import models
from django.contrib.auth.models import User

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def summaryT(self):
        return self.title[:10]

    def summaryB(self):
        return self.content[:30]

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol=models.ForeignKey(Jasoseol, on_delete=models.CASCADE)
