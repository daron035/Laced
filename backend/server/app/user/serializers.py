from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        print(
            " wqeiurioqwueriowqueriouqwioeruioquweiroqwioerWERIUIQOETIUWERITOUWIERUTIWEJKJJ"
        )
        # request = self.context.get("request")
        # sessionid = request.COOKIES.get("sessionid", None)
        # if sessionid:
        #     print(sessionid)
        #     representation["sessionid"] = sessionid
        return representation
