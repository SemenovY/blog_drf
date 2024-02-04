import logging

from celery import shared_task
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from subscriptions.models import Subscription
from users.models import BlogPost

logger = logging.getLogger(__name__)


@shared_task
def send_daily_newsletter():
    try:
        current_datetime = timezone.now()
        subscriptions = Subscription.objects.all()

        for subscription in subscriptions:
            user = subscription.user
            blog_posts = BlogPost.objects.filter(blog__in=subscription.blog).order_by("-created_at")[:5]

            if blog_posts:
                html_content = render_to_string("daily_newsletter.html", {"blog_posts": blog_posts})
                text_content = strip_tags(html_content)

                logger.info(
                    f"Ежедневная подборка постов от {current_datetime} для пользователя {user.username}:\n{text_content}"
                )
    except Exception as e:
        logger.error(f"An error occurred in send_daily_newsletter: {str(e)}")
