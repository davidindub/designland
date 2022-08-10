from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Resource
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormForResource


class ResourceList(generic.ListView):
    model = Resource
    queryset = Resource.objects.filter(approved=True)
    template_name = "index.html"
    paginate_by = 9


class TagList(ResourceList):
    """
    View for showing all the resources with a specified tag
    """

    def get_queryset(self):

        return Resource.objects.filter(approved=True).filter(tags__name__in=[self.kwargs["tag"]])


class BookmarkList(ResourceList):
    """
    View for showing all the resources the logged in user has bookmarked
    """

    def get_queryset(self):

        # Filter to return only the resources bookmarked by the logged in user
        return Resource.objects.filter(approved=True).filter(bookmarks__in=[self.request.user.id])


class UserProfile(View):
    def get(self, request, *arg, **kwargs):
        if "user" in self.kwargs:
            user_profile = get_object_or_404(
                User, username=self.kwargs["user"])
        else:
            user_profile = get_object_or_404(
                User, username=request.user.username)

        return render(
            request,
            "user_profile.html",
            {
                "user_profile": user_profile
            }
        )


class ListByUser(ResourceList):
    """
    View for showing all the resources added by a user
    """

    def get_queryset(self):
        user_id = User.objects.get(username=self.kwargs["user"]).id

        return Resource.objects.filter(approved=True).filter(author__id__in=[user_id])


class CreateResource(View):
    """
    View for form for adding a resource in the database
    """

    def get(self, request):
        form = FormForResource()
        context = {"form": form}

        return render(request, "resource_form.html", context)

    def post(self, request, *arg, **kwargs):
        form = FormForResource(request.POST)
        if form.is_valid():
            new_entry = form.save()
            # Should return user to the details page of the resource they just added or updated
            return redirect("resource_detail", new_entry.slug)

class UpdateResource(View):
    """
    View for form for updating a resource in the database
    """

    def get(self, request, *arg, **kwargs):
        if "slug" in self.kwargs:
            resource = get_object_or_404(
                Resource, slug=self.kwargs["slug"])
            form = FormForResource(instance=resource)

            context = {"form": form}

        return render(request, "resource_form.html", context)

    def post(self, request, *arg, **kwargs):
        resource = get_object_or_404(
                Resource, slug=self.kwargs["slug"])

        form = FormForResource(request.POST, instance=resource)

        if form.is_valid():
            updated_entry = form.save()
            # Should return user to the details page of the resource they just added or updated
            return redirect("resource_detail", updated_entry.slug)



class ResourceDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Resource.objects.filter(approved=True)
        resource = get_object_or_404(queryset, slug=slug)
        comments = resource.comments.filter(
            approved=True).order_by("created_on")
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
