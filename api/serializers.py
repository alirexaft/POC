from rest_framework import serializers


class LoginWithPasswordSerializer(serializers.Serializer):  # noqa
    username = serializers.CharField(max_length=100, min_length=5, required=True)
    password = serializers.CharField(max_length=100, min_length=5, required=True)

    def validate_username(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value

    def validate_password(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value