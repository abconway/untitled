from rest_framework import routers

from title.views import TitleViewSet


router = routers.SimpleRouter()
router.register(r'titles', TitleViewSet)
urlpatterns = router.urls
