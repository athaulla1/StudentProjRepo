from django.db import models

class Student(models.Model):

    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=70)
    sm1=models.IntegerField()
    sm2=models.IntegerField()
    sm3=models.IntegerField()
    tot = models.IntegerField()


    def __str__(self):
        return self.sname
