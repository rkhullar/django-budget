from django.db.models import Model, CharField, DecimalField, TextField


class Product(Model):
    name = CharField(max_length=200)
    unit_price = DecimalField(decimal_places=2, max_digits=10)
    description = TextField(null=True, blank=True)


# class Budget(Model):
#     owner = ForeignKey(User, on_delete=CASCADE)
#     created = DateTimeField(auto_now=True)
#     updated = DateTimeField(auto_now=True)
#
#     # TODO: add method to get total
#
#
# class BudgetLine(Model):
#     product = ForeignKey(Product, on_delete=CASCADE)
#     quantity = IntegerField(default=1)
#     budget = ForeignKey(Budget, on_delete=CASCADE)
#
#     # TODO: add method to get subtotal
