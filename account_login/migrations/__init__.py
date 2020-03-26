from django.db import models
from django.contrib.auth.models import User
from account_login.views import increment_account_number


account_id = models.BigIntegerField(default=increment_account_number, unique=True)
account_id.contribute_to_class(User, 'account_id')

