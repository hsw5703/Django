from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import Helloworld


def hello_world(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

# 로그인 과정
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # 로그인했는지, 또 로그인한 사람과 요청한 유저 정보와 동일한지 확인
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()  # 금지된 페이지에 접근했다는 걸 명시.

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()