from .models import UserDetails
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id', 'name', 'email', 'telephone', 'username' )