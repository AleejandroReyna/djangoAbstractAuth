from django.urls import path
from users.views import CreateUserApiView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserApiView.as_view(), name='create')
]
