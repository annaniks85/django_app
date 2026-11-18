from typing import Sequence

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="ul Kopernika, d 8",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(f"Created order {order}")


#class Command(BaseCommand):

    #@transaction.atomic
    #def handle(self, *args, **options):
        #self.stdout.write("Create order with products")
        #user = User.objects.get(username="john")
        # products: Sequence[Product] = Product.objects.defer(
        #     "description",
        #     "price",
        #     "created_at",
        # ).all()
        #products: Sequence[Product] = Product.objects.only("id").all()
        #order, created = Order.objects.get_or_create(
            #delivery_address="ul Ivanova, dom 22, kv 8",
            #promocode="promo5",
            #user=user,
        #)
        #for product in products:
            #order.products.add(product)
        #self.stdout.write(f"Created order {order}")
