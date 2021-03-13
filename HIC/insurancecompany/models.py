from django.db import models

class Company(models.Model):
    insurance_company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    details = models.TextField()


    def __str__(self):
        return self.name
