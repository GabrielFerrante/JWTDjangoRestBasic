from django.db import models

# Create your models here.

class Card(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='cards',
        null=True
    )


class Task(models.Model):

    description = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    card = models.ForeignKey(Card, related_name='tasks', on_delete=models.CASCADE)