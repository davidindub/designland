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


class ResourceDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Resource.objects.filter(approved=True)
        resource = get_object_or_404(queryset, slug=slug)
        comments = resource.comments.filter(approved=True).order_by("created_on")
        
        bookmarked = False
        if resource.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True
        
        return render(
            request,
            "resource_detail.html",
            {
                "resource": resource,
                "comments": comments,
                "bookmarked": bookmarked
            }
        )


class ResourceLike(View):

    def resource(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Post, slug=slug)
        if resource.bookmarks.filter(id=request.user.id).exists():
            resource.bookmarks.remove(request.user)
        else:
            resource.bookmarks.add(request.user)

        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))