from .models import Car
from django.urls import reverse_lazy
from .forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView



class CarListView(ListView):
    model = Car
    template_name = 'car_view.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        if search := self.request.GET.get('search'):
            cars = cars.filter(model__icontains=search)
        return cars
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required, name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = '/cars/cars/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # associa o usuário logado
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/cars/'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)