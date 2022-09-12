from django.urls import path
from .views import News, NewsDetail, Search, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
    path('', News.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', Search.as_view(), name='news_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]