from django.urls import path
from .views import GenericAPIView

urlpatterns = [

    path('generic/programs/', GenericAPIView.as_view()),
    path('generic/programs/<int:id>/', GenericAPIView.as_view()),

]