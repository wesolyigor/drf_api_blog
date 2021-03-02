from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from posts.models import Post


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='testpass123',
        )
        test_post = Post.objects.create(author=testuser1, title='fajny post', body="bopdy bosdy bodfyh")

    def test_blog_content(self):
        post = Post.objects.last()

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'fajny post')
        self.assertEqual(body, 'bopdy bosdy bodfyh')