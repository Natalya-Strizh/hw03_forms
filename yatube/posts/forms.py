from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': _('Post_text'),
            'group': _('Post_group')
        }
        help_texts = {
            'name': _('Текст поста, обязательное для заполнения поле'),
            'name': _('Группа для поста, необязательное для заполнения поле')
        }
