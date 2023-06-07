from django import forms
from .models import Comunicado
from django.utils import timezone


class ComunicadoForm(forms.ModelForm):
    # Acá se crea un formulario para crear o actualizar el comunicado

    def clean(self):
        # Este método se llama durante la validación del formulario y permite realizar modificación o validación de los datos.
        cleaned_data = super().clean()

        cleaned_data['fecha_envio'] = timezone.now().date()
        # Establecer el campo fecha_envio de los datos limpios con la fecha actual usando timezone.now().date().
        # Esto asegura que el campo fecha_envio se complete automáticamente con la fecha actual.

        return cleaned_data
        # Devolver los datos limpios modificados.

    class Meta:
        # La clase Meta proporciona información adicional sobre el formulario.
        model = Comunicado
        # Especifica el modelo con el que está asociado el formulario, en este caso, el modelo Comunicado.
        fields = ['titulo', 'detalle', 'categoria', 'nivel']
        # Define los campos que se incluirán en el formulario.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener las opciones de nivel definidas en el modelo Comunicado
        nivel_choices = Comunicado.NIVEL_CHOICES
        # Establecer el campo "nivel" del formulario como un ChoiceField con las opciones de niveles del modelo
        self.fields['nivel'] = forms.ChoiceField(choices=nivel_choices)

