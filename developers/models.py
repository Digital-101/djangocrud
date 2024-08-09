from django.db import models

# Create your models here.
class Developer(models.Model):
    lid = models.CharField(max_length=20)
    dname = models.CharField(max_length=100)
    demail = models.EmailField()
    contact = models.CharField(max_length=10)
    class Meta:
        db_table = 'developers'