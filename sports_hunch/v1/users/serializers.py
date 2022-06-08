from rest_framework import serializers

from v1.users.models import User


class ActiveUsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
