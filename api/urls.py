from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .accounts.views import UserViewSet, CreateOrganizationView


router = DefaultRouter()

router.register('accounts', UserViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
    path('create-organization', CreateOrganizationView.as_view()),
    path('login/', obtain_jwt_token),
]