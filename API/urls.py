from django.conf.urls import url, include
from .views import StatusViewset, TasksViewset, CategoryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TasksViewset, basename='tasks')
router.register('status', StatusViewset, basename='status')
router.register('caterogy', CategoryViewset, basename='category')

urlpatterns = [
    url('', include(router.urls)),

]