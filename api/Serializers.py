from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSeriallizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'list', 'done']


class ListSeriallizer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSeriallizer(many=True)

    class Meta:
        model = List
        fields = ['name', 'owner', 'url', 'item_set']

