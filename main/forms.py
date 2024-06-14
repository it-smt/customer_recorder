from django import forms


class RecordForm(forms.Form):
    """Форма записи."""
    pk_service = forms.IntegerField(widget=forms.HiddenInput())
    pk_master = forms.IntegerField(widget=forms.HiddenInput())
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия',
    }))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Отчество',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Номер телефона',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Электронная почта',
    }))
