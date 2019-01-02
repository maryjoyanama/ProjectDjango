from rest_framework import viewsets
from .models import Posts
from .serializers import PostsSerializer
from datetime import date, datetime

class PostsViewSet(viewsets.ModelViewSet):
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer

class PostsStatusSuccessViewSet(viewsets.ModelViewSet):
	queryset = Posts.objects.filter(status='Success')
	serializer_class = PostsSerializer

class PostsStatusFailedViewSet(viewsets.ModelViewSet):
	queryset = queryset = Posts.objects.filter(status='Failed')
	serializer_class = PostsSerializer

class BadgeStatusSuccessViewSet(viewsets.ModelViewSet):
	queryset = Posts.objects.exclude(status='Failed') & Posts.objects.exclude(lastcomplete_date__lt=date(2018, 12, 1))
	serializer_class = PostsSerializer

class BadgeStatusFailedViewSet(viewsets.ModelViewSet):
	queryset = Posts.objects.exclude(status='Success') & Posts.objects.exclude(lastcomplete_date__lt=date(2018, 12, 1))
	serializer_class = PostsSerializer
