from django.db import models`

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()

    def __str__(self):
        return self.title