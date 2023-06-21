import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from apps.models import Category


@pytest.mark.django_db
def test_get_task(api_client) -> None:
    payload = {
        'name': 'Food'
    }
    url = reverse_lazy('category-list')
    response = api_client.get(url, payload, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_task(api_client) -> None:
    payload = {
        'name': 'Food'
    }
    url = reverse_lazy('category-list')
    response = api_client.post(url, payload)
    print(response)
    category = Category.objects.first()
    assert response.status_code == status.HTTP_201_CREATED
    assert category is not None
    assert category.name == payload['name']


def test_pytest_working():
    assert True == True
