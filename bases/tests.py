from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostTest(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'hidden'
        )
        self.post = Post.objects.create(
            title = 'A good blog',
            body = 'Nice cool blog body',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good blog')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice cool blog body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice cool blog body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good blog')
        self.assertTemplateUsed(response, 'post_detail.html')

