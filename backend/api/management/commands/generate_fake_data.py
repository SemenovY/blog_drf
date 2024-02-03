from random import randint
from uuid import uuid4

from api.constants import MAX_POSTS_PER_BLOG, NUM_USERS
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from users.models import Blog, BlogPost, CustomUser

User = CustomUser


class Command(BaseCommand):
    help = "Generate fake data for testing purposes"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start generating fake data..."))

        fake = Faker()

        for _ in range(NUM_USERS):
            username = f"user_{uuid4()}"
            user, created = User.objects.get_or_create(username=username, password="password123")

            blog, blog_created = Blog.objects.get_or_create(user=user)

            if blog_created:
                num_posts = randint(1, MAX_POSTS_PER_BLOG)
                for _ in range(num_posts):
                    title = fake.sentence()
                    text = fake.paragraph()
                    created_at = timezone.now()

                    BlogPost.objects.create(blog=blog, title=title, text=text, created_at=created_at)

        self.stdout.write(self.style.SUCCESS(f"{NUM_USERS} пользователей с блогами и постами успешно созданы."))
