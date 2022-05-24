from django.db import models

CATEGORY_CHOICES = (
    ('C', 'construction'),
    ('W', 'welding'),
    ('G', 'general'),
    ('P', 'paints'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    
)



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=1)
    label = models.CharField(choices = LABEL_CHOICES, max_length=1)
    

    def __str__(self):
        return self.title
