from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = "THIS is the test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "THIS is the test!")

    def test_url_exists_at_correct_location(self):  # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):  # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "home.html")

        self.assertContains(response, "THIS is the test!")

