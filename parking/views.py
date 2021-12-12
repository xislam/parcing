from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from parking.forms import ParkingForm, MyUserCreationForm
from parking.models import Parking


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:

            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


class ParkingList(LoginRequiredMixin, ListView):
    paginate_by = 50
    template_name = 'index.html'
    context_object_name = 'parking'
    model = Parking


class ParkingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Parking
    form_class = ParkingForm

    def get_success_url(self, *args):
        messages.success(self.request, " Создано !")
        return reverse('index')


class ParkingUpdateView(LoginRequiredMixin, UpdateView):
    model = Parking
    template_name = 'update.html'
    form_class = ParkingForm
    context_object_name = 'update'

    def get_success_url(self):
        messages.success(self.request, f"Обновлено !")
        return reverse('index')


class ParkingDeleteView(LoginRequiredMixin, DeleteView):
    model = Parking

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f"Удалино !")
        return reverse('index')


class ReserveParkingView(LoginRequiredMixin, View):
    model = Parking

    def get(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Parking, id=pk)
        obj.user = request.user
        obj.save()
        messages.add_message(request, messages.INFO, 'Your reservation successfully completed.')
        return redirect('index')


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


