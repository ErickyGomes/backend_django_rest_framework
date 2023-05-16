from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'items', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='My API title'))
]