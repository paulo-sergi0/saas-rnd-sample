import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    #queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count()
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def about_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_template = "about.html"
    return render(request, html_template, my_context)