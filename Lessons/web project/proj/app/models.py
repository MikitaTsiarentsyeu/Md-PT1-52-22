from email.mime import image
from django.db import models

class Author(models.Model):

    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, primary_key=True)

class Post(models.Model):

    POST_THEMES = [('n', 'nature'), ('t', 'technology'), ('s', 'sport')]

    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads')
    issued = models.DateTimeField()
    post_theme = models.CharField(choices=POST_THEMES, max_length=1, blank=False)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

