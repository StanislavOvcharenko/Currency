from rest_framework.test import APIClient
from rest_framework.reverse import reverse


def test_contactus_api_get():
    client = APIClient()
    response = client.get(reverse('api-v1:contactuslist'))
    assert response.status_code == 200
    assert response.json()[0]['id']


def test_contactus_create_api_post_empty():
    client = APIClient()
    response = client.post(reverse('api-v1:contactuscreate'), data={})
    assert response.status_code == 400
    assert response.json() == {'email_from': ['This field is required.'],
                               'email_to': ['This field is required.'],
                               'subject': ['This field is required.'],
                               'message': ['This field is required.']
                               }
    # breakpoint()


def test_contactus_create_api_post(mailoutbox):
    data = {'email_from': 'admin@admin.com',
            'email_to': 'admin@admin.com',
            'subject': 'example',
            'message': 'example text'
            }
    client = APIClient()
    response = client.post(reverse('api-v1:contactuscreate'), data=data)
    assert response.status_code == 201
    assert response.json() == {'id': 11, 'email_from': 'admin@admin.com', 'email_to': 'admin@admin.com',
                               'subject': 'example', 'message': 'example text'}
    assert len(mailoutbox) == 1


def test_contactus_create_api_invaliddata():
    data = {'email_from': 'adminadmin.com',
            'email_to': 'adminadmin.com',
            'subject': 'example',
            'message': 'example text',
            }
    client = APIClient()
    response = client.post(reverse('api-v1:contactuscreate'), data=data)
    # breakpoint()
    assert response.status_code == 400
    assert response.json() == {'email_from': ['Enter a valid email address.'],
                               'email_to': ['Enter a valid email address.']}


def test_contactus_details_api():
    client = APIClient()
    response = client.get(reverse('api-v1:contactus', args=[8]))
    assert response.status_code == 200
    assert response.json()
