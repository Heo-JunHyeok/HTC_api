from django.db import models


# Create your models here.
class Health(models.Model):
    health = models.CharField(max_length=20)
    icon = models.URLField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.health


class Count(models.Model):
    health = models.ForeignKey(Health, on_delete=models.CASCADE, related_name="counts")
    count = models.IntegerField()
    date = models.DateField()
