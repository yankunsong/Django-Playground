from django.http import HttpResponse


def index(req):
    return HttpResponse("Hello! You're at the poll index.")
