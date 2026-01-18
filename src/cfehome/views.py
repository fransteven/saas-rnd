from django.shortcuts import render

from visits.models import PageVisits


def home(request, *args, **kwargs):
    path = request.path

    queryset = PageVisits.objects.all()
    my_title = "My Page"
    html_template = "home.html"
    my_context = {"my_title": my_title, "queryset": queryset, "path": path}
    PageVisits.objects.create()
    return render(request, html_template, my_context)
