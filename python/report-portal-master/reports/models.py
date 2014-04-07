from django.db import models

# Create your models here.
class ProfitPeport(models.Model):
		moment = models.CharField(max_length=13)
		profit = models.FloatField()
		first_cost = models.FloatField()
		minutes = models.FloatField()
		

