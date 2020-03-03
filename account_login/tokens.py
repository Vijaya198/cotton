from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from allauth.account.models import EmailAddress


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(EmailAddress.verified)

        )



account_activation_token = AccountActivationTokenGenerator()

class PasswordTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(EmailAddress.verified)

        )



password_reset_token = PasswordTokenGenerator()