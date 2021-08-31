from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('recent_posts.html')
def render_recent_blogposts():
    return {
        # This is just an example query, your actual models may vary
        'post_list': Post.objects.filter(status=1).order_by('-created_on')[:6]
    }






    