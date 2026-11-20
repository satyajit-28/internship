from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    biography = models.TextField()
    nationality = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Author"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Book"

    def __str__(self):
        return self.title

    


