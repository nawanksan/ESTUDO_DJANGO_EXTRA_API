from django.db import models

class Author(models.Model):
    name = models.CharField
    birth_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return super().__str__()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return super().__str__()