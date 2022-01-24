from django import forms


class InputSeriesForm(forms.Form):
    series = forms.CharField(label='Название модели', max_length=50)

