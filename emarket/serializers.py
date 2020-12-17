from rest_framework import serializers
from .models import Category, Item, Item_Image
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


# api for category
class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=20)
    class Meta:
        model = Category
        fields = '__all__'


# api for item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class Item_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Image
        fields = '__all__'

# api for user
class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


# model serializer only needed fields
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
