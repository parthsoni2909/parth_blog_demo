
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from blog.models import Blog,Category,Tag

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'
class BlogCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class BlogTagListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'