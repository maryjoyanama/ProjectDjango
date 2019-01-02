from django.contrib import admin
from django.urls import include, path
from .routers import router
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
	path('posts', include('posts.urls')),	
    path('posts', TemplateView.as_view(template_name='posts/index.html'))
]
