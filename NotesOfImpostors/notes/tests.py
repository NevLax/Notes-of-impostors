from django.test import TestCase


# Create your tests here.
class AuthTest(TestCase):

    def test_protected_page(self):
        response = self.client.get("/note/1/")
        self.assertEqual(response.status_code, 302)
