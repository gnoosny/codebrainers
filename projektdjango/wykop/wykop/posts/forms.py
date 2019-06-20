from wykop.posts.models import Comment

from django.forms.models import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']