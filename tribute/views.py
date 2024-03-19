from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "tribute.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = [
            "Environment",
            "Humanitarian",
            "Animal",
            "Health and Disease",
        ]
        context["sliders"] = [
            {
                "title": "🌍 Environment",
                "description": "Supports various environmental charities.",
                "name": "environment",
            },
            {
                "title": "🤝 Humanitarian",
                "description": "Supports various humanitarian charities.",
                "name": "humanitarian",
            },
            {
                "title": "🐾 Animal",
                "description": "Supports various animal charities.",
                "name": "animal",
            },
            {
                "title": "❤️ Health and Disease",
                "description": "Support charities that develop novel treatments and cures, and help those suffering with disease.",
                "name": "health",
            },
        ]
        return context
