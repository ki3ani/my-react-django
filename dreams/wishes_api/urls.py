from django.urls import path
from .views import PostList, PostDetail



app_name = 'wishes_api'


urlpatterns = [
    path('wishes/', PostList.as_view(), name='post_list'),
    path('wishes/<int:pk>/', PostDetail.as_view(), name='post_detail')
]

