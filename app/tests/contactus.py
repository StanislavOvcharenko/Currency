from django.urls import reverse
import pytest


def test_contactus_get(client):
    response = client.get(reverse('currency:contactus_create'))
    assert response.status_code == 200


def test_contactus_post_empty(client):
    response = client.post(reverse('currency:contactus_create'), data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_from': ['This field is required.'],
                                                    'email_to': ['This field is required.'],
                                                    'subject': ['This field is required.'],
                                                    'message': ['This field is required.']}


def test_contactus_post_valid(client, mailoutbox):
    data = {'email_from': 'admin@admin.com',
            'email_to': 'admin@admin.com',
            'subject': 'admin@admin.com',
            'message': 'Hello'}
    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 302
    assert len(mailoutbox) == 1


@pytest.mark.parametrize('email_from', ('adminadmin', '213113', 'fagasgas'))
def test_contactus_post_invalid_email(client, email_from):
    data = {'email_from': email_from,
            'email_to': 'admin@admin.com',
            'subject': 'admin@admin.com',
            'message': 'Hello'}
    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_from': ['Enter a valid email address.']}
