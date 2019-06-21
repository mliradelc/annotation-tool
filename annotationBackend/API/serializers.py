from rest_framework import serializers
from API.models import User, Video, Category, Label, Track, Annotation, Comment
from django.contrib.auth.models import User as djangoUser

class UserAPISerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'access', 'created_at',
                'updated_at', 'deleted_at',
                'usr_created', 'usr_updated', 'usr_deleted')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'extid', 'access', 'created_at', 'updated_at', 'deleted_at', 
                'created_by', 'updated_by', 'deleted_by')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'access', 'created_at', 'updated_at', 'deleted_at',
                'created_by', 'updated_by', 'deleted_by', 'description', 'has_duration',
                'settings', 'video')
    
class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label





class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = djangoUser
        fields = ('url', 'id', 'username')