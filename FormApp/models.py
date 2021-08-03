from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    picture = models.FileField(upload_to='picture/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'
