from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormForResource, FormForProfile
from .models import Resource, Profile


class ResourceList(generic.ListView):
    model = Resource
    queryset = Resource.objects.filter(approved=True)
    template_name = "resources_list.html"
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
            user_info = get_object_or_404(
                User, username=self.kwargs["user"])
            profile_info = get_object_or_404(
                Profile, user=user_info.id)
        else:
            user_info = get_object_or_404(
                User, username=request.user.username)
            profile_info = get_object_or_404(
                Profile, user=request.user.id)

        return render(
            request,
            "user_profile.html",
            {
                "user_info": user_info,
                "profile_info": profile_info
            }
        )


class UpdateUserProfile(View):
    """
    View for form for updating a user profile in the database
    """

    def get(self, request, *arg, **kwargs):
        print(f"🟩 SLUG IS {self.kwargs['user']} 🟩")
        
        if "user" in self.kwargs:
            user_info = get_object_or_404(
                User, username=self.kwargs["user"])

            profile_info = get_object_or_404(
                Profile, user=user_info.id)

            if self.request.user.id == user_info.id or self.request.user.is_superuser:

                form = FormForProfile(instance=profile_info)

                context = {"form": form}

                return render(request, "user_profile_form.html", context)

        # else:
        #     return redirect("home")

    def post(self, request, *arg, **kwargs):
        user_info = get_object_or_404(
            User, username=self.kwargs["user"])
        profile_info = get_object_or_404(
            Profile, user=user_info.id)

        if self.request.user.id == user_info.id or self.request.user.is_superuser:

            form = FormForProfile(request.POST, instance=profile_info)

            if form.is_valid():
                updated_entry = form.save()
                # Return user to the profile they just updated
                return redirect("user", user_info.username)

        else:
            return redirect("home")


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
        if self.request.user.is_authenticated:
            form = FormForResource()
            context = {"form": form}

            return render(request, "resource_form.html", context)

        else:
            return redirect("home")

    def post(self, request, *arg, **kwargs):
        if self.request.user.is_authenticated:
            form = FormForResource(request.POST)
            if form.is_valid():
                new_entry = form.save()
                # Should return user to the details page of the resource
                # they just added or updated
                return redirect("resource_detail", new_entry.slug)
            else:
                return render(request, "resource_form.html", {"form": form})

        else:
            return redirect("home")


class UpdateResource(View):
    """
    View for form for updating a resource in the database
    """

    def get(self, request, *arg, **kwargs):
        if "slug" in self.kwargs:
            resource = get_object_or_404(
                Resource, slug=self.kwargs["slug"])

            if self.request.user == resource.author or self.request.user.is_superuser:

                form = FormForResource(instance=resource)

                context = {"form": form}

                return render(request, "resource_form.html", context)

            else:
                return redirect("home")

    def post(self, request, *arg, **kwargs):
        resource = get_object_or_404(
            Resource, slug=self.kwargs["slug"])

        if self.request.user == resource.author or self.request.user.is_superuser:

            form = FormForResource(request.POST, instance=resource)

            if form.is_valid():
                updated_entry = form.save()
                # Should return user to the details page of the resource they just added or updated
                return redirect("resource_detail", updated_entry.slug)

        else:
            return redirect("home")


class DeleteResource(View):
    def get(self, request, slug, *arg, **kwargs):
        resource = get_object_or_404(
            Resource, slug=self.kwargs["slug"])

        if self.request.user == resource.author or self.request.user.is_superuser:
            return render(request, "resource_delete.html", {"resource": resource})

        else:
            return redirect("home")

    def post(self, request, *arg, **kwargs):
        resource = get_object_or_404(
            Resource, slug=self.kwargs["slug"])

        if self.request.user == resource.author or self.request.user.is_superuser:
            resource.delete()

        return redirect("home")


class ResourceDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Resource.objects.filter(approved=True)
        resource = get_object_or_404(queryset, slug=slug)
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

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
