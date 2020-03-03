from rest_framework import routers
from allauthuserapp import api_views

router = routers.DefaultRouter()
router.register('profile',api_views.UserProfileViewSet)
# router.register('login',api_views.UserLoginApiView)
