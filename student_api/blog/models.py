from django.db import models

# Create your models here.
class Blog(models.Model):
        title = models.CharField(max_length=30)
        description = models.TextField()
        content = models.TextField()

class Comment(models.Model):
        blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name="comments")
        comment = models.TextField(null=True, blank=True)
