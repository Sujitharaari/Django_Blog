from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to='images/', blank=True)
    Content = models.TextField()

class Contact(models.Model):
    Your_Name = models.CharField(max_length=200)
    Email_Address = models.EmailField()
    Phone = models.IntegerField()
    Subject = models.TextField()
    Your_Message = models.TextField()