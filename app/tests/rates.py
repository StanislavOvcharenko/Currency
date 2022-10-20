from django.urls import reverse


def test_rate_list(client):
    response = client.get(reverse('currency:rate_list'))
    assert response.status_code == 302


def test_rate_list_get_page(client):
    response = client.get(f"{reverse('currency:rate_list')}?page=2")
    assert response.status_code == 302
