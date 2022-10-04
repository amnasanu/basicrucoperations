from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet


router = DefaultRouter()
router.register('article',ArticleViewSet, basename='article'),


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    # path('',views.articleview , name = 'articleview'),
    # path('details/<int:pk>/',views.articleView, name = 'articleView'),
    # path('',views.ArticleAPIView.as_view()),
    # path('details/<int:id>/',views.ArticleDetails.as_view()),
    path('details/<int:id>/',views.GenericAPIView.as_view()),

]