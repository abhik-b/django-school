from django.db import models

# Create your models here.


class Classs(models.Model):
    name = models.CharField(max_length=50)
    total_days = models.IntegerField(default=100, blank=True, null=True)
    criteria = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True, default=0.75)

    def __str__(self):
        return self.name

    def days_atleast(self):
        return int(self.total_days*self.criteria)

    def criteria_percent(self):
        return int(self.criteria*100)
