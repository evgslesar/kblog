from django import template
from blog.models import Post, Tags

register = template.Library()


@register.inclusion_tag('blog/carusel_tpl.html')
def show_carusel(cnt=5):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}

