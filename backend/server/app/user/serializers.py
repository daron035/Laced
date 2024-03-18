from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
        )
