from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ResourceList.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('details/<slug:slug>/', views.ResourceDetail.as_view(),
         name='resource_detail'),
    path('add/', views.CreateResource.as_view(), name='create_resource'),
    path('details/<slug:slug>/update/', views.UpdateResource.as_view(),
         name='update_resource'),
    path('tag/<slug:tag>/', views.TagList.as_view(), name='tag'),
    path('user/', views.UserProfile.as_view(), name='user'),
    path('user/<slug:user>/', views.UserProfile.as_view(), name='user'),
    path('user/<slug:user>/added/',
         views.ListByUser.as_view(), name='added_by_user'),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks'),
    path('bookmark/<slug:slug>', views.ResourceBookmark.as_view(),
         name='bookmark_resource'),
    path('upvote/<slug:slug>', views.ResourceUpvote.as_view(),
         name='upvote_resource'),
]
