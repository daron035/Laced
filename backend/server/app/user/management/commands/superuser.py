from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creates a superuser account"

    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(first_name="root").exists():
            User.objects.create_superuser(
                email="root@mail.ru", first_name="root", last_name="root", password="1"
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
            print("asdfsd")
