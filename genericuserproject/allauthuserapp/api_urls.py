from django.urls import path, include
from allauthuserapp import api_views
from allauthuserapp import api_routers

urlpatterns = [
    path('v1/',include(api_routers.router.urls)),
    path('token/',api_views.UserLoginApiView.as_view()),
]
