from django import forms
from .models import Plato
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class PlatoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlatoCreateForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Guardar'))
        self.fields['lista_ingredientes'].widget.attrs['rows'] = 1
        self.fields['descripcion'].widget.attrs['rows'] = 3

    class Meta:
        model = Plato
        fields = ('nombre', 'lista_ingredientes', 'descripcion', 'precio', 'foto')