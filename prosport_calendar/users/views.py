import django.contrib.auth
import django.contrib.auth.mixins
import django.views

import users.forms

class Registration(django.views.View):
    form_class = users.forms.SignUpForm
    template_name = "users/signup.html"

    def get(self, request):
        form = users.forms.SignUpForm()
        context = {
            "form": form,
        }
        return django.shortcuts.render(request, self.template_name, context)


    def post(self, request):
        form = users.forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return django.shortcuts.redirect("users:login")
        context = {"form": form}
        return django.shortcuts.render(request, self.template_name, context)

class Profile(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.View,
):
    template_name = "users/profile.html"

    def get(self, request):
        user = request.user
        profile_form = users.forms.ProfileUpdateForm(
            instance=user.profile,
        )
        context = {
            "profile_form": profile_form,
        }
        return django.shortcuts.render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        profile_form = users.forms.ProfileUpdateForm(
            request.POST or None,
            request.FILES or None,
            instance=user.profile,
        )
        if profile_form.is_valid():
            profile_form.save()
            request.session.modified = True
            django.contrib.messages.success(
                request,
                "Настройки сохранены.",
            )
            return django.shortcuts.redirect("users:profile")

        context = {
            "profile_form": profile_form,
        }
        return django.shortcuts.render(
            request,
            self.template_name,
            context,
        )
