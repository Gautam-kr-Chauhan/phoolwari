from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


class Flower(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_option=[('Artificial','Artificial'),
                 ('Natural','Natural')
                 ]
    type=models.CharField(max_length=20,choices=type_option)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
    seasonality_option = [
        ('Spring','Spring'),
        ('Summer','Summer'),
        ('Autumn','Autumn'),
        ('Winter','Winter')
    ]

    seasonality=models.CharField(max_length=20,choices=seasonality_option)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="flower_images")
    vase_life=models.CharField(max_length=100)
    def __str__(self):
        return self.name