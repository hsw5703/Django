from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')
        # input_txt라는 이름을 가진 hello_world.html의 값을 가져온다.
        return render(request, 'accountapp\hello_world.html',
                      context={'text': temp})
    else:
        return render(request, 'accountapp\hello_world.html',
                      context={'text':'GET METHOD!'})