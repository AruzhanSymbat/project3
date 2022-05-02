from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name
class Posts(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.title
class Nature(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.title
class User(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length = 50)
    picture = models.ImageField()
    nickname = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    about = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name
