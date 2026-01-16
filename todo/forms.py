from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description','is_completed']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Judul Tugas'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Deskripsi (opsional)'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }