from rest_framework import serializers
from API.models import User
from django.contrib.auth.models import User as djangoUser

class UserAPISerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'access', 'created_at',
                'updated_at', 'deleted_at',
                'usr_created', 'usr_updated', 'usr_deleted')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = djangoUser
        fields = ('url', 'id', 'username')