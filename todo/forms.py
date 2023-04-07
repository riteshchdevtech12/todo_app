from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed',)
        widgets = {'author': forms.HiddenInput()}

    def save(self, commit=True, author=None):
        if author:
            self.instance.author = author
        return super().save(commit)