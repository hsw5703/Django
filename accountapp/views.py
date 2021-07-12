from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import Helloworld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')
        # input_txt라는 이름을 가진 hello_world.html의 값을 가져온다.

        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp\hello_world.html',
                      context={'hello_world_list': hello_world_list})