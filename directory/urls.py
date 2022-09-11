from . import views
from django.views.generic import TemplateView
from django.urls import path, include

resource_patterns = [
    path('', views.ResourceDetail.as_view(), name='resource_detail'),
    path('approve/', views.ApproveResource.as_view(),
         name='approve_resource'),
    path('update/', views.UpdateResource.as_view(), name='update_resource'),
    path('delete/', views.DeleteResource.as_view(), name='delete_resource')
]

user_patterns = [
    path('', views.UserProfile.as_view(), name="user"),
    path('added/', views.ListByUser.as_view(), name='added_by_user'),
    path('update/', views.UpdateUserProfile.as_view(),
         name='update_user_profile'),
    path('delete/', views.DeleteUserProfile.as_view(),
         name='delete_user_profile'),
]

list_patterns = [
    path('', views.ResourceList.as_view(), name='listall'),
    path('unapproved/', views.UnapprovedList.as_view(), name='unapproved'),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks'),
    path('tag/<slug:tag>/', views.TagList.as_view(), name='tag'),
    path('<slug:filter>/', views.ResourceList.as_view(), name="list")
]

urlpatterns = [
    path('', TemplateView.as_view(template_name="splash_page.html"), name='home'),
    path('list/', include(list_patterns)),
    path('accounts/', include('allauth.urls')),
    path('manage/users', views.ProfilesList.as_view(), name='profile_list'),
    path('add/', views.CreateResource.as_view(), name='create_resource'),
    path('resource/<slug:slug>/', include(resource_patterns)),
    path('user/', views.UserProfile.as_view(), name='user'),
    path('user/<slug:user>/', include(user_patterns), name='user'),
    path('bookmark/<slug:slug>', views.ResourceBookmark.as_view(),
         name='bookmark_resource'),
    path('upvote/<slug:slug>', views.ResourceUpvote.as_view(),
         name='upvote_resource'),
    path('alltags/', views.GetAllTags.as_view(), name="alltags"),
    path('privacy/', TemplateView.as_view(template_name="privacy_policy.html"), name='privacy'),
]
