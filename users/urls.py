from django.urls import path, include
from .views import RegisterView, logout


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/logout/', logout),
    path('register/', RegisterView.as_view()),
]