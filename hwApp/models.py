from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    published = models.DateField()
    def __str__(self):
        return self.title
