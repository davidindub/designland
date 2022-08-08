from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Resource
from django.contrib import messages


class ResourceList(generic.ListView):
    model = Resource
    queryset = Resource.objects.filter(approved=True).order_by("upvotes")
    template_name = "index.html"
    paginate_by = 9

class TagList(ResourceList):
    def get_queryset(self):

        return Resource.objects.filter(approved=True).filter(tags__name__in=[self.kwargs["tag"]]).order_by("upvotes")

class BookmarkList(ResourceList):
    def get_queryset(self):

        # Filter to return only the resources bookmarked by the logged in user
        return Resource.objects.filter(approved=True).filter(bookmarks__in=[self.request.user.id])

class ResourceDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Resource.objects.filter(approved=True)
        resource = get_object_or_404(queryset, slug=slug)
        comments = resource.comments.filter(approved=True).order_by("created_on")
        content = resource.content
        tags = resource.tags.all()
        
        bookmarked = False
        if resource.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        upvoted = False
        if resource.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        
        return render(
            request,
            "resource_detail.html",
            {
                "resource": resource,
                "comments": comments,
                "bookmarked": bookmarked,
                "upvoted": upvoted,
                "tags": tags
            }
        )


class ResourceBookmark(View):

    def post(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Resource, slug=slug)
        if resource.bookmarks.filter(id=request.user.id).exists():
            resource.bookmarks.remove(request.user)
        else:
            resource.bookmarks.add(request.user)

        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))


class ResourceUpvote(View):

    def post(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Resource, slug=slug)
        if resource.upvotes.filter(id=request.user.id).exists():
            resource.upvotes.remove(request.user)
        else:
            resource.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))