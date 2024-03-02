from django.urls import path
from . import views

urlpatterns = [
    # path('blog-list/',views.blog_list,name='blog_list'),
    # path('blog-details/<int:pk>/',views.blog_details,name='blog_details'),

    # class base views URLS
    path('blog-list/',views.BlogListView.as_view(),name='blog_list'),
    path('blog-details/<int:pk>/',views.BlogDetailView.as_view(),name='blog_details'),

]