from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import register, UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'project-members', ProjectMemberViewSet, basename='project-member')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('users/register/', register, name='user-register'),
] + router.urls
