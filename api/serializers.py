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


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100, min_length=5)
    password = serializers.CharField(required=True, max_length=100, min_length=5)
    first_name = serializers.CharField(required=False, max_length=50, min_length=3)
    last_name = serializers.CharField(required=False, max_length=50, min_length=3)

    def validate_username(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value

    def validate_password(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value

    def validate_first_name(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value

    def validate_last_name(self, value):
        if value is None:
            raise serializers.ValidationError("this field can't be null")
        return value
