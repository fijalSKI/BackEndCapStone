from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Menu, Booking

class MenuTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-list')
        self.menu_data = {'name': 'Pizza', 'description': 'Delicious pizza', 'price': 9.99}

    def test_create_menu(self):
        response = self.client.post(self.menu_url, self.menu_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking_url = reverse('booking-list')
        self.booking_data = {'first_name': 'John', 'reservation_date': '2023-10-10', 'reservation_slot': '18:00'}

    def test_create_booking(self):
        response = self.client.post(self.booking_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
