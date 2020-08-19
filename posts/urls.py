from django.urls import path
from .views import *


app_name="posts"
urlpatterns=[
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('show/<int:id>/', show, name="show"),
    path('edit/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('create_comment/<int:post_id>/', create_comment, name="create_comment")
]

