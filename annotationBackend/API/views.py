from API.models import User, Video, Category
from API.serializers import UserAPISerializer, VideoSerializer, CategorySerializer
from rest_framework import generics
#from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserAPISerializer

class VideoViewSet(viewsets.ModelViewSet):
    """
    This endpoint gives information about the videos registered in the annotation tool.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoryVieWSet(viewsets.ModelViewSet):
    """
    Endpoint in charge to manage the categories in each video of the annotation tool.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


""" @api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'videos': reverse('videos-list', request=request, format=format),
        'categories': reverse('categories-list', request=request, format=format)
    }) """
