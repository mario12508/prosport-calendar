from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

import meropriations.parser
from meropriations.models import Meropriation


class Home(ListView):
    template_name = "homepage/main.html"
    context_object_name = "meropriations"

    def get_queryset(self):
        return Meropriation.objects.select_related('group', 'structure',
                                                   'tip').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(self.get_queryset(),
                              10)
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return context


class UpdateDBView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения этой операции."
            )
        meropriations.parser.f()
        return HttpResponse("База данных успешно обновлена.")
