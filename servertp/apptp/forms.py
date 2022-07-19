from django import forms

class Empresa_formulario(forms.Form):

    empresa = forms.CharField(max_length=250)
    dedicacion = forms.CharField(max_length=250)

    def __str__(self):
        return f'{self.empresa} / {self.dedicacion}'

class Empleado_formulario(forms.Form):
    
    nombre_completo = forms.CharField(max_length=250)
    puesto = forms.CharField(max_length=250)
    empresa_trabajo = forms.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre_completo} / {self.puesto}'

class Producto_formulario(forms.Form):

    nombre_producto = forms.CharField(max_length=250)
    producto_empresa = forms.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre_producto}'
