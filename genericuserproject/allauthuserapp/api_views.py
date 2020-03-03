from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import IsAuthenticated

from allauthuserapp import models
from allauthuserapp import api_permissions
from allauthuserapp import api_serializers

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating Users Profile"""
    serializer_class = api_serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (
            api_permissions.UpdateOwnProfile,
            IsAuthenticatedOrReadOnly
        )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email','mobile_no',)

class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
