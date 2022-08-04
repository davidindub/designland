from . import views
from django.urls import path

urlpatterns = [
    path('', views.ResourceList.as_view(), name='home'),
    path('<slug:slug>/', views.ResourceDetail.as_view(), name='resource_detail'),
    path('bookmark/<slug:slug>', views.ResourceLike.as_view(),
         name='bookmark_resource'),
]
