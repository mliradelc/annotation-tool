from API.models import User
from API.serializers import UserAPISerializer
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

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })

@api_view(['POST'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })

@api_view(['PUT'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })

@api_view(['DELETE'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })