from django.test import TestCase, Client
from django.urls import reverse
from ..models import FlashUser

# Create your tests here.
class MainPageTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @classmethod
    def setUpTestData(self):
        for user in range(1, 15):
            user = FlashUser.objects.create(username=f'Tester{user}', is_active=True, full_name=f'Tester John{user}', email=f'user{user}@gmail.com')
            user.set_password('super_password')
        print('setUpTest data: Success')
        pass
    def test_status(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_reverse_request(self):
        respose = self.client.get(reverse('home'))
        self.assertEqual(respose.status_code, 200)

    def test_template_name(self):
        respose = self.client.get(reverse('home'))
        self.assertTemplateUsed(respose, 'base.html')

    def test_user_amout(self):
        request = self.client.get(reverse('home'))
        self.assertTrue('posts' in request.context)

    def test_user_amout(self):
        request = self.client.get(reverse('home'))
        self.assertTrue('add_post_form' in request.context)

    def test_is_not_loggined(self):
        request = self.client.get('/profile/2')
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/login/?next=/profile/2')

    def test_is_loggined(self):
        print(FlashUser.objects.all()[3])
        self.client.login(username='Tester4', password='super_password')
        response = self.client.get('/profile/2')
        self.assertEqual(response.status_code, 200)