from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import Helloworld


@login_required(login_url=reverse_lazy('accountapp:login'))
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

has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')  # 함수에 사용하는 decorator를 method에도 사용가능하도록 변환해준다.
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})

    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'