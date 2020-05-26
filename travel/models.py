from django.db import models

class destination(models.Model): #attributes
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    def __str__(self):
        return self.name

