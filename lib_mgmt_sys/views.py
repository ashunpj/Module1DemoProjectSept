from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def sample_view(request):
    #
    # return HttpResponse('Hi, I am a view!!')
    user = 'shreyansh'
    friends = ['ram', 'sita', 'hari', 'gita']
    return render(request, 'index.html', context={'user_name': user, 'friends': friends})


def gallery(request):

    return render(request, 'gallery.html')