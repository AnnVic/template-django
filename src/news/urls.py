from django.urls import path
from .views import ListArticle, ListCategory, ArticleDetail, CategoryDetail

#urlpatterns = [
#path("articles/", ListArticle.as_view(), name="articles"),
#path("articles/<int:pk>/", ArticleDetail.as_view(), name="article"),
#path("categories/", ListCategory.as_view(), name="categories"),
#path("categories/<int:pk>/", CategoryDetail.as_view(), name="category"),
#]