from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser account"

    def handle(self, *args, **options):
        User = get_user_model()

        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "category.json", "variation.json", "variation_option.json", "product.json", "image.json", "currency.json", "country.json")

        if not User.objects.filter(first_name="root").exists():
            User.objects.create_superuser(
                email="root@mail.ru", first_name="root", password="1",
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
