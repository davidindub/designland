from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from .forms import FormForResource, FormForProfile
from .models import Resource, Profile


class ResourceList(generic.ListView):
    model = Resource
    template_name = "resources_list.html"
    paginate_by = 9

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()

        results = {
            "unapproved": qs.filter(approved=False),
            "approved": qs.filter(approved=True),
            "bookmarks": qs.filter(approved=True).filter(bookmarks__in=[self.request.user.id]),
        }

        if "listby" in self.kwargs:
            return results[self.kwargs["listby"]]

        # Filter to display approved resources
        return qs.filter(approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["h1"] = "Default h1"

        h1s = {"unapproved": "Unapproved Resources",
               "approved": "Approved Resources",
               "bookmarks": "Your bookmarks",
               }

        if "listby" in self.kwargs:
            context["h1"] = h1s[self.kwargs["listby"]]

        return context


class TagList(ResourceList):
    """
    View for showing all the resources with a specified tag
    """

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        # Filter to display approved resources with the requested tag
        return qs.filter(approved=True).filter(tags__name__in=[self.kwargs["tag"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["h1"] = f"#{self.kwargs['tag']}"
        return context


class BookmarkList(ResourceList):
    """
    View for showing all the resources the logged in user has bookmarked
    """

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        # Filter to return only the resources bookmarked by the logged in user
        return qs.filter(approved=True).filter(bookmarks__in=[self.request.user.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["h1"] = "Your bookmarks"
        return context


class ListByUser(ResourceList):
    """
    View for showing all the resources added by a user
    """

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        user_id = User.objects.get(username=self.kwargs["user"]).id
        # Filter to display approved added by the queried user
        return qs.filter(approved=True).filter(author__id__in=[user_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["h1"] = f"Added by {self.kwargs['user']}"
        return context


class UserProfile(View):
    """
    View for a user's profile page
    """

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

        context = {
            "user_info": user_info,
            "profile_info": profile_info,
            "h1": f"{profile_info}"}

        return render(request, "user_profile.html", context)


class UpdateUserProfile(View):
    """
    View for form for updating a user profile in the database
    """

    def get(self, request, *arg, **kwargs):

        if "user" in self.kwargs:
            user_info = get_object_or_404(
                User, username=self.kwargs["user"])

            profile_info = get_object_or_404(
                Profile, user=user_info.id)

            if self.request.user.id == user_info.id or self.request.user.is_superuser:

                form = FormForProfile(instance=profile_info)

                context = {"form": form, "user_info": user_info}

                return render(request, "user_profile_form.html", context)

        else:
            return redirect("home")

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
                messages.add_message(
                    request, messages.SUCCESS, 'Profile Updated!')
                return redirect("user", user_info.username)

        else:
            return redirect("home")


class DeleteUserProfile(View):
    def get(self, request, *arg, **kwargs):
        user_info = get_object_or_404(
            User, username=self.kwargs["user"])
        profile_info = get_object_or_404(
            Profile, user=user_info.id)

        if self.request.user == user_info or self.request.user.is_superuser:

            context = {"user_info": user_info, "profile_info": profile_info}

            return render(request, "user_profile_delete.html", context)

        else:
            return redirect("home")

    def post(self, request, *arg, **kwargs):
        user_info = get_object_or_404(
            User, username=self.kwargs["user"])

        if self.request.user == user_info or self.request.user.is_superuser:
            messages.add_message(request, messages.SUCCESS,
                                 f"Account for {user_info} successfully deleted.")
            user_info.delete()

        return redirect("home")


class CreateResource(View):
    """
    View for form for adding a resource in the database
    """

    def get(self, request):
        if self.request.user.is_authenticated:
            form = FormForResource()
            context = {"form": form, "h1": "Submit a new Design Resource"}

            return render(request, "resource_form.html", context)

        else:
            return redirect("home")

    def post(self, request, *arg, **kwargs):
        print(self.request.user.id)
        if self.request.user.is_authenticated:
            user_info = get_object_or_404(User, id=self.request.user.id)
            form = FormForResource(request.POST)
            if form.is_valid():
                # Set the author to the logged in user
                form.instance.author = self.request.user

                form.instance.slug = slugify(form.instance.title)

                new_entry = form.save()
                messages.add_message(
                    request, messages.SUCCESS, f"{new_entry} successfully added.")
                # return user to the details page of the resource
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

                context = {"form": form, "h1": f"Update {resource}"}

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
                messages.add_message(
                    request, messages.SUCCESS, f"{resource} updated.")
                # return user to the details page of the resource they added or updated
                return redirect("resource_detail", updated_entry.slug)

        else:
            messages.add_message(request, messages.ERROR,
                                 f"There was an error")
            return redirect("home")


class DeleteResource(View):
    def get(self, request, slug, *arg, **kwargs):
        resource = get_object_or_404(
            Resource, slug=self.kwargs["slug"])

        context = {"resource": resource}

        if self.request.user == resource.author or self.request.user.is_superuser:
            return render(request, "resource_delete.html", context)

        else:
            return redirect("home")

    def post(self, request, *arg, **kwargs):
        resource = get_object_or_404(
            Resource, slug=self.kwargs["slug"])

        if self.request.user == resource.author or self.request.user.is_superuser:
            resource.delete()

        return redirect("home")


class ApproveResource(View):

    def post(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Resource, slug=slug)

        if self.request.user.is_staff:
            if not resource.approved:
                resource.approved = True
                messages.add_message(request, messages.SUCCESS,
                                     f"{resource} approved")
            else:
                resource.approved = False
                messages.add_message(
                    request, messages.INFO, f"{resource} hidden")

            resource.save()

        return redirect("resource_detail", resource.slug)


class ResourceDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Resource.objects.filter()
        resource = get_object_or_404(queryset, slug=slug)
        tags = resource.tags.all()

        context = {
            "resource": resource,
            "approved": True if resource.approved else False,
            "bookmarked": True if resource.bookmarks.filter(id=self.request.user.id).exists() else False,
            "upvoted": True if resource.upvotes.filter(id=self.request.user.id).exists() else False,
            "tags": tags
        }

        if (resource.approved is False):
            if (resource.author == self.request.user or self.request.user.is_superuser):
                return render(request, "resource_detail.html", context)
            else:
                raise Http404

        elif (resource.approved):
            return render(request, "resource_detail.html", context)

        else:
            raise Http404


class ResourceBookmark(View):

    def post(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Resource, slug=slug)
        if resource.bookmarks.filter(id=request.user.id).exists():
            resource.bookmarks.remove(request.user)
            messages.add_message(request, messages.INFO, "Bookmark Removed")
        else:
            resource.bookmarks.add(request.user)
            messages.add_message(request, messages.INFO,
                                 f"Bookmarked {resource}.")

        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))


class ResourceUpvote(View):

    def post(self, request, slug, *args, **kwargs):
        resource = get_object_or_404(Resource, slug=slug)
        if resource.upvotes.filter(id=request.user.id).exists():
            messages.add_message(request, messages.INFO,
                                 f"Removed upvote from {resource}.")
            resource.upvotes.remove(request.user)
        else:
            messages.add_message(request, messages.INFO,
                                 f"Upvoted {resource}!")
            resource.upvotes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ProfilesList(generic.ListView):
    """
    View for admin view of all user profiles
    """
    model = Profile
    template_name = "profile_list.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()

        return qs.order_by("user__date_joined")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["h1"] = "Users sorted by join date"

        return context