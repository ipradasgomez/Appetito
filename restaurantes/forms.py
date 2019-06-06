from django import forms
from .models import Restaurante
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class RestauranteCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestauranteCreateForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Guardar'))

    class Meta:
        model = Restaurante
        fields = ('nombre', 'descr', 'telefono', 'email', 'logo', 'banner')

class RestauranteEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestauranteEditForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Guardar'))

    class Meta:
        model = Restaurante
        fields = ('nombre', 'descr', 'telefono', 'email', 'logo', 'banner')