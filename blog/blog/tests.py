from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.
class Blogtest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'olokor',
            email='olokorwisdom15@gmail.com',
            password='12345'
            )
        
        self.post = Post.objects.create(
            title ='a good title',
            body = 'a good body',
            author = self.user
            
            )
    def test_string_representation(self):
        self.assertEqual(f'{self.post.title}','a good title')
        self.assertEqual(f'{self.post.author}', 'olokor') 
        self.assertEqual(f'{self.post.body}', 'a good body')
    
    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a good body')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detailview(self):
       response=self.client.get('/post/1/')
       no_response = self.client.get('/post/10000/')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(no_response.status_code, 404)
       self.assertContains(response, 'a good title')
       self.assertTemplateUsed(response, 'post_detail.html')