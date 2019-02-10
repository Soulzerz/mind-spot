from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    """ Represents the Tag model """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class Category(models.Model):
    """ Represents the Category model """
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class Post(models.Model):
    """ Represents the Post model """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    """ Represents the Post's Comment model """
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    def __repr__(self):
        return self.text
    
    def approve(self):
        self.approved = True
        self.save()
    