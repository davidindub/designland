from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ResourceList.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('resource/<slug:slug>/', views.ResourceDetail.as_view(), name='resource_detail'),
    path('bookmark/<slug:slug>', views.ResourceBookmark.as_view(),
         name='bookmark_resource'),
    path('upvote/<slug:slug>', views.ResourceUpvote.as_view(),
         name='upvote_resource'),
]
