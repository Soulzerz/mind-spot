from django.test import TestCase, RequestFactory
from .models import Post, Category, Tag
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Soulz', email='Soulz@gmail.com', password='ultra_secret_password')
        Post.objects.create(title='Test Title', author=self.user, created_date=timezone.now(), text='A very long time ago a text was created to test something!')
        Post.objects.create(title='Test Title the Sequel', author=self.user, created_date=timezone.now(), text='A very long time ago a text was created to test something once more!')

    def test_post_publish(self):
        first_post = Post.objects.get(title='Test Title')
        second_post = Post.objects.get(title='Test Title the Sequel')
        author = User.objects.get(username='Soulz')
        #self.assertIs(first_post.author, author)
        self.assertIs(second_post.text, 'A very long time ago a text was created to test something once more!')