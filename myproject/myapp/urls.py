from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, ServiceRequestViewSet, register, user_login, user_logout, dashboard, submit_request, register_api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("submit-request/", submit_request, name="submit_request"),
    path("api/", include(router.urls)),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", register_api, name="register_api"),
]

