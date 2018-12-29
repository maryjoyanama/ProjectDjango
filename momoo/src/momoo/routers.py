from rest_framework import routers
from posts.viewsets import PostsViewSet, PostsStatusSuccessViewSet, PostsStatusFailedViewSet, BadgeStatusSuccessViewSet, BadgeStatusFailedViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'statussuccess', PostsStatusSuccessViewSet)
router.register(r'statusfailed', PostsStatusFailedViewSet)
router.register(r'badgestatussuccess', BadgeStatusSuccessViewSet)
router.register(r'badgestatusfailed', BadgeStatusFailedViewSet)