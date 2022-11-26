from django.db import models

class Ebooks(models.Model):
    genre_opt=(
        ('List of Fantasy','List of Fantasy'),
        ('Literary','Literary'),
        ('Mystery','Mystery'),
        ('Non-Fiction','Non-Fiction'),
        ('Science Fiction','Science Fiction'),
        ('Thriller','Thriller')
    )
    review_opt=(
        ('*','one star'),
        ('**','two star'),
        ('***','three star'),
        ('****','four star'),
        ('*****','five star')
    )
    book_title=models.TextField(max_length=150)
    author=models.TextField(max_length=150)
    genres=models.CharField(choices=genre_opt,max_length=120)
    review=models.CharField(choices=review_opt,max_length=50)
    favorite=models.BooleanField(default=True)

