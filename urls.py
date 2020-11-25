from django.conf.urls import url,include
from .views import ProgCategoryviewsets,ProgSeriesviewsets,programsviewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ProgramCatogary', ProgCategoryviewsets,basename="Catogary")
router.register(r'ProgramSeries', ProgSeriesviewsets,basename="Series")
router.register(r'Programs', programsviewsets, basename="programs")


urlpatterns = [
    url('', include(router.urls)),
]
