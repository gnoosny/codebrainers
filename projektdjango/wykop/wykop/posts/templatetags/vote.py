from django import template

from wykop.posts.models import Vote

register = template.Library()

@register.simple_tag(takes_context=True)
def user_vote(context):
    return Vote.objects.filter(
        user=context['user'],
        post=context['post'],
        value=context['value']
    ).exists()