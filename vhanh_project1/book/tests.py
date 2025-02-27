# book/tests/test_permissions.py
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from customer.models import Customer
from book.models import Book

@pytest.mark.django_db
def test_customer_permissions():
    client = APIClient()

    # Tạo customer và đăng nhập
    customer = Customer.objects.create_user(username='customer1', password='pass1234', email='customer@test.com')
    client.login(username='customer1', password='pass1234', backend='customer.backends.CustomerAuthBackend')

    book = Book.objects.create(title='Test Book', author='Author 1', price=100)

    url = reverse('book-detail', args=[book.id])

    # Customer chỉ được GET
    get_response = client.get(url)
    assert get_response.status_code == 200

    post_response = client.post(reverse('book-list'), {'title': 'New Book', 'author': 'Author 2', 'price': 150})
    assert post_response.status_code == 403

    put_response = client.put(url, {'title': 'Updated Book', 'author': 'Author 1', 'price': 120})
    assert put_response.status_code == 403

    delete_response = client.delete(url)
    assert delete_response.status_code == 403
