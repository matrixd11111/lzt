from django.forms import ModelForm

from .models import ( Client,
                      Orders,
                      Service, 
)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'surname',
            'third_name',
            'birth_date',
            'phone_number',
            'note',
            'email',
            'patient',
            'client_type',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = [
            'order_service',
            'order_performer',
            'order_note',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            x = self.fields[fields_name]
            print(dir(x))
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            'service_name',
            'service_cod',
            'service_note',
            'service_price',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

