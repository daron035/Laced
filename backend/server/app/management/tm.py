# from django.db import models
# from django.contrib.sessions.models import Session
#
# from app.product.models import Account, Product
# from app.user.models import UserAccount
#
#
# from django.contrib.sessions.models import Session
#
#
# class Cart(models.Model):
#     # session = models.ForeignKey(Session, on_delete=models.CASCADE)
#     session = models.ForeignKey(
#         Session, null=True, blank=True, on_delete=models.SET_NULL
#     )
#     # session = models.CharField(max_length=100, null=True)
#     # account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="cart")
#     # items = models.ManyToManyField("CartItem", related_name="cart")
#
#     user = models.ForeignKey(
#         UserAccount,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="cart",
#     )
#     # session = models.ForeignKey(
#     #     Session, null=True, blank=True, on_delete=models.CASCADE
#     # )
#
#     # def delete(self, *args, **kwargs):
#     #         self.slug = slugify(self.name)
#     #     return super().save(*args, **kwargs)
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # , related_name='item'
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField(default=1)
#     added = models.DateTimeField(auto_now_add=True)
