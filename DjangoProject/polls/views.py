from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey this is my first Polls inded in django! Are u there?")