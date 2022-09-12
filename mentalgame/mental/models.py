from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MentalGameResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField()
    questions = models.IntegerField()
    speed=models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user)
    
class QuantitativeSpsec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    quantitativeSps=models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField(auto_now=True)

class VerbalSpsec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    verbalSps=models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField(auto_now=True)
    