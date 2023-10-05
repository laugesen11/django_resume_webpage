from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class HomePageTest(SimpleTestCase):
    # Set up the base test
    def setUp(self):
        self.name_response = self.client.get(reverse('home'))
 
    # Test that we crrectly resolve the base page
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
 
    # Test that we correctly resolve the homepage by name
    def test_home_page_by_name(self):   
        self.assertEqual(self.name_response.status_code, 200)

    # Test that we get the correct template
    def test_correct_template(self):
        self.assertTemplateUsed(self.name_response, 'home.html')
    

class TestSignupTest(TestCase):
    # The data we use to create a user
    username = 'testuser'
    email = 'testuser@email.com'

    # Set up the test data
    def setUp(self):
        self.signup_response = self.client.get(reverse('signup'))
        self.signup_template = 'signup.html'

    # Confirms our name URL works
    def test_get_url_by_name(self):
        self.assertEqual(self.signup_response.status_code, 200) 
 
    # Confirms we get the correct template with our signup
    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.signup_response, self.signup_template)

    # Confirms the base path for signup works and gets the correct template
    def test_url_path_works(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.signup_template)

    # Tests that the signup for works
    def test_signup_form(self):
        # Makes a new user
        new_user = get_user_model().objects.create_user(self.username, self.email) 

        # Confirms we greated the new user
        self.assertEqual(get_user_model().objects.all().count(), 1)        

        # Confirms the new user values match what we expect
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
