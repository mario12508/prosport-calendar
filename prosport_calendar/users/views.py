import django.contrib.auth
from django.contrib.auth.views import LoginView
import django.contrib.auth.mixins
import django.views

import users.forms
import meropriations.models


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = users.forms.CustomLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти в аккаунт'
        return context


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
        context = {

        }
        context["genders"] = ["Муж.", "Жен."]
        context['tips'] = (
            meropriations.models.Meropriation.objects
            .values_list('tip__name', flat=True)
            .distinct()
            .order_by('tip__name')  # Optional: to ensure consistent ordering
        )
        context['groups'] = (
            meropriations.models.Meropriation.objects
            .values_list('group__name', flat=True)
            .distinct()
            .order_by('group__name')  # Optional: to ensure consistent ordering
        )
        context['structures'] = (
            meropriations.models.Meropriation.objects
            .values_list('structure__name', flat=True)
            .distinct()
            .order_by('structure__name')
        )
        tip = request.GET.get("tip")
        gender = request.GET.get("gender")
        group = request.GET.get("group")
        structure = request.GET.get("structure")

        if (tip is None and gender is None
                and group is None and structure is None):
            request.GET.tip = user.profile.tip_request
            request.GET.gender = user.profile.gender_request
            request.GET.group = user.profile.group_request
            request.GET.structure = user.profile.structure_request
        else:
            user.profile.tip_request = request.GET.get("tip")
            user.profile.gender_request = request.GET.get("gender")
            user.profile.group_request = request.GET.get("group")
            user.profile.structure_request = request.GET.get("structure")
            user.profile.save()
        context['request'] = request

        return django.shortcuts.render(request, self.template_name, context)
