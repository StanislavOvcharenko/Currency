import uuid
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'password1',
        )

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password1']:
                raise forms.ValidationError('Password missmatch')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = str(uuid.uuid4())
        instance.is_active = False
        instance.set_password(self.cleaned_data['password'])

        if commit:
            instance.save()

        self._send_activation_email()

        return instance

    def _send_activation_email(self):
        subject = 'Activate account'
        message = f'''
        Activation link: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{reverse('accounts:activate',
                                                                            args=(self.instance.username,))}'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [self.instance.email],
            fail_silently=False,
        )
