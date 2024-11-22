import django.views.generic

import meropriations.parser

class Home(django.views.generic.ListView):
    template_name = "homepage/main.html"
    context_object_name = "items"
    queryset = [
        {
            "id": 1,
            "name": "first",
        },
        {
            "id": 2,
            "name": "second",
        },
    ]

    def get_context_data(self, **kwargs):
        meropriations.parser.f()

