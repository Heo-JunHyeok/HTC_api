from django.db import models


# Create your models here.
class Training(models.Model):
    name = models.CharField(max_length=20)
    icon = models.URLField()

    def __str__(self):
        return self.name


class Count(models.Model):
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE, related_name="counts"
    )
    number = models.IntegerField()
    date = models.DateField()
