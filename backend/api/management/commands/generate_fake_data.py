from random import randint

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from faker import Faker

from users.models import Blog, BlogPost

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake data for testing purposes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start generating fake data...'))

        num_users = 50
        max_posts_per_blog = 10

        fake = Faker()

        for _ in range(num_users):
            # Создаем пользователя с уникальным именем на основе времени
            username = f'user_{timezone.now().strftime("%Y%m%d%H%M%S")}'
            user, created = User.objects.get_or_create(username=username, password='password123')

            # Получаем или создаем блог для пользователя
            blog, blog_created = Blog.objects.get_or_create(user=user)

            if blog_created:
                # Генерируем случайное количество постов для блога
                num_posts = randint(1, max_posts_per_blog)
                for _ in range(num_posts):
                    title = fake.sentence()
                    text = fake.paragraph()
                    created_at = timezone.now()

                    # Создаем пост для блога
                    BlogPost.objects.create(blog=blog, title=title, text=text, created_at=created_at)

        self.stdout.write(self.style.SUCCESS(f'{num_users} пользователей с блогами и постами успешно созданы.'))
