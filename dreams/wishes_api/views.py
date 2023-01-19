from rest_framework import generics
from wishes.models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostDetailSerializer


