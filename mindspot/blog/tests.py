from django.test import TestCase, RequestFactory, Client
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
        second_post.publish()
        author = User.objects.get(username='Soulz')
        self.assertEqual(first_post.author, author)
        self.assertEqual(first_post.published_date, None)

        self.assertNotEqual(second_post.published_date, None)
        self.assertEqual(second_post.text, 'A very long time ago a text was created to test something once more!')

    def test_get_home(self):
        c = Client()
        response = c.get('/')
        self.assertTrue(response.status_code == 200)
    
    def test_get_post_detail(self):
        c = Client()
        post =  Post.objects.get(title='Test Title')
        response = c.get('/post/{}'.format(post.pk))
        self.assertTrue(response.status_code == 200)
    
    def test_get_post_edit(self):
        c = Client()
        post =  Post.objects.get(title='Test Title')
        response = c.get('/post/{}/edit'.format(post.pk))
        self.assertTrue(response.status_code == 200)

    def test_get_post_delete(self):
        c = Client()
        post =  Post.objects.get(title='Test Title')
        response = c.get('/post/{}/delete'.format(post.pk))
        self.assertTrue(response.status_code == 302)



class Category(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Soulz', email='Soulz@gmail.com', password='ultra_secret_password')
        
