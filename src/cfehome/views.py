from django.shortcuts import render

from visits.models import PageVisits


def home(request, *args, **kwargs):
    path = request.path

    queryset = PageVisits.objects.all()
    my_title = "My Page"
    my_context = {"my_title": my_title, "queryset": queryset, "path": path}
    PageVisits.objects.create()
    html_template = "home.html"
    return render(request, html_template, my_context)
