from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from app.product.models import Product


class Command(BaseCommand):
    help = "Creates a superuser account"

    def handle(self, *args, **options):
        customer_group, created = Group.objects.get_or_create(name="customer")
        print(customer_group.name)
        # manager_group, created = Group.objects.get_or_create(name="Manager")
        # admin_group, created = Group.objects.get_or_create(name="Admin")

        content_type = ContentType.objects.get_for_model(Product)
        post_permission = Permission.objects.filter(content_type=content_type)

        print(content_type)
        print(post_permission)
        # for perm in post_permission:
        #     customer_group.permissions.add(perm)
        #
        # group_permissions = customer_group.permissions.all()
        #
        # # Вывод разрешений в консоль
        # for permission in group_permissions:
        #     print(permission.codename)
