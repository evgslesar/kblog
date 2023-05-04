from django import template
from blog.models import Post, Tags

register = template.Library()

@register.inclusion_tag('blog/recent_posts_tpl.html')
def get_recent(cnt=5):
    posts = Post.objects.all()[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/tags_posts_tpl.html')
def get_tags(cnt=5):
    tags = Tags.objects.all()
    return {"tags": tags}