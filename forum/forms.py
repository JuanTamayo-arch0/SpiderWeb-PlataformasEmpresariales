# forum/forms.py

from django import forms
from .models import Post, Reply, Board

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título del post'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje...'}),
        }


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Escribe tu respuesta aquí...'})
        }


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['nombre', 'slug', 'categoria', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción del board'}),
        }
