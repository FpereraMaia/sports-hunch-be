from django.db import models

from users.models import User


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
