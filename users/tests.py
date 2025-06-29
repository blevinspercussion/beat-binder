from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersRoutesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')
        self.user_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpass123',
        }
        self.user = User.objects.create_user(
            email=self.user_data['email'],
            first_name=self.user_data['first_name'],
            last_name=self.user_data['last_name'],
            password=self.user_data['password'],
        )

    def test_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

    def test_signup_post_valid(self):
        data = {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'newpass123',
        }
        response = self.client.post(self.signup_url, data, follow=True)
        self.assertRedirects(response, '/about/')
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())
        self.assertTrue(response.context['user'].is_authenticated)

    def test_signup_post_invalid(self):
        data = {'email': '', 'first_name': '', 'last_name': '', 'password': ''}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')
        self.assertFalse(User.objects.filter(email='').exists())

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')

    def test_login_post_valid(self):
        data = {'username': self.user_data['email'], 'password': self.user_data['password']}
        response = self.client.post(self.login_url, data, follow=True)
        self.assertRedirects(response, '/about/')
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_post_invalid(self):
        data = {'username': self.user_data['email'], 'password': 'wrongpass'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')
        self.assertFalse(response.context['user'].is_authenticated)

    def test_logout(self):
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(response.context['user'].is_authenticated)

    def test_profile_authenticated(self):
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_data['email'])

    def test_profile_unauthenticated_redirect(self):
        response = self.client.get(self.profile_url, follow=True)
        self.assertRedirects(response, f"{self.login_url}?next={self.profile_url}")

    def test_routes_exist(self):
        for url in [self.signup_url, self.login_url, self.logout_url, self.profile_url]:
            response = self.client.get(url)
            # logout redirects, profile redirects if not logged in
            self.assertIn(response.status_code, [200, 302])
