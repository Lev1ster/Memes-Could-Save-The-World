from django.urls import path
from .views import UserCreateOrListView, UserView

urlpatterns = [
    path(
        '<int:pk>/',
        UserView.as_view(),
        name='user-operate-view'
    ),
    path(
        '',
        UserCreateOrListView.as_view(),
        name='user-create-or-list'
    ),
]