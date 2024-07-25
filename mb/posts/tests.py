from django.test import TestCase
from .models import posts
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        posts.objects.create(text='testin the db')

    def test_text_content(self):
        post=posts.objects.get(id=1)
        expected_object = f'{post.text}'
        self.assertCountEqual(expected_object, 'testin the db')

class HomePageViewTest(TestCase):
    def setUp(self):
        posts.objects.create(text='nother test')

    def test_view_respense_nbr(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_view_respense_nbr_Byname(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_view_UsesCorrect_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

