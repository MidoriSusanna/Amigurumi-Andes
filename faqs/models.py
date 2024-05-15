from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField()

    def __str__(self):
        return self.question

