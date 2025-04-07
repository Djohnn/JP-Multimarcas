from django import forms
from .models import Brand, Car




class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'model': ('Modelo'),
            'brand': ('Marca'),
            'factory_year': ('Ano de fabricação'),
            'model_year': ('Ano do modelo'),
            'plate': ('Placa'),
            'value': ('Valor R$'),
            'photo': ('Foto'),
        }

    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor não pode ser menor que R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação não pode ser menor que 1975')
        return factory_year
    
