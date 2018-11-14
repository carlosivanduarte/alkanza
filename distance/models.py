from django.db import models

class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1000, blank=True, default='')
    latitude = models.DecimalField(blank=False, decimal_places=20, max_digits=50)
    longitude = models.DecimalField(blank=False, decimal_places=20, max_digits=50)
    radius = models.IntegerField(blank=False)
    calculation = models.DecimalField(blank=False, decimal_places=2, max_digits=50)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name