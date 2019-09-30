from django.urls import path
from users.views import CreateUserApiView, UpdateUserApiView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserApiView.as_view(), name='create'),
    path('<int:user_id>/update/', UpdateUserApiView.as_view(), name='update')
]
