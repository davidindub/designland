from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ResourceList.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('add/', views.CreateResource.as_view(), name='create_resource'),
    path('tag/<slug:tag>/', views.TagList.as_view(), name='tag'),
    path('resource/<slug:slug>/', include([
        path('', views.ResourceDetail.as_view(), name='resource_detail'),
        path('approve/', views.ApproveResource.as_view(),
             name='approve_resource'),
        path('update/', views.UpdateResource.as_view(), name='update_resource'),
        path('delete/', views.DeleteResource.as_view(), name='delete_resource')
    ])),
    path('user/', views.UserProfile.as_view(), name='user'),
    path('user/<slug:user>/', include([
        path('', views.UserProfile.as_view(), name='user'),
        path('added/', views.ListByUser.as_view(), name='added_by_user'),
        path('update/', views.UpdateUserProfile.as_view(),
             name='update_user_profile'),
        path('delete/', views.DeleteUserProfile.as_view(),
             name='delete_user_profile'),
    ])),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks'),
    path('bookmark/<slug:slug>', views.ResourceBookmark.as_view(),
         name='bookmark_resource'),
    path('upvote/<slug:slug>', views.ResourceUpvote.as_view(),
         name='upvote_resource')
]
