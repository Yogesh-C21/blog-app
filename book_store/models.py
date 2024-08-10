from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
#define the bluprint of the table

class Country(models.Model):
    country = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

class Address(models.Model):
    street =models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    postal_code =models.CharField(max_length=255)

    def full_address(self):
        return f"{self.street}, {self.city} - {self.postal_code}"

    def __str__(self):
        return self.full_address()
    

class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    # one to one relationship
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title =models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    #  ONE TO MANY Relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)

    published_countries = models.ManyToManyField(Country)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def book_title(self):
        return f"{self.title}"

    def __str__(self):
        return self.book_title()
