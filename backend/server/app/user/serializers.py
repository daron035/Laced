from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_staff",
        )

    #     fields = tuple(User.REQUIRED_FIELDS) + (
    #         settings.USER_ID_FIELD,
    #         settings.LOGIN_FIELD,
    #     )
    #     read_only_fields = (settings.LOGIN_FIELD,)
    #
    # def update(self, instance, validated_data):
    #     email_field = get_user_email_field_name(User)
    #     instance.email_changed = False
    #     if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
    #         instance_email = get_user_email(instance)
    #         if instance_email != validated_data[email_field]:
    #             instance.is_active = False
    #             instance.email_changed = True
    #             instance.save(update_fields=["is_active"])
    #     return super().update(instance, validated_data)
