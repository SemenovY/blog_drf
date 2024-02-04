from random import randint
from uuid import uuid4

from api.constants import NUM_USERS, POSTS_PER_DAY
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

        try:
            for _ in range(NUM_USERS):
                username = f"user_{uuid4()}"
                user, created = User.objects.get_or_create(username=username, password="password123")
                blog, blog_created = Blog.objects.get_or_create(user=user)
                num_posts = POSTS_PER_DAY * randint(1, 3)
                for _ in range(num_posts):
                    title = fake.sentence()
                    text = fake.paragraph()
                    created_at = timezone.now()
                    user = blog.user
                    BlogPost.objects.create(user=user, blog=blog, title=title, text=text, created_at=created_at)

            self.stdout.write(self.style.SUCCESS(f"{NUM_USERS} пользователей с блогами и постами успешно созданы."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
