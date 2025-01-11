from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
# Importing the OrderLineItem model to listen for changes


# Signal (@receiver) listens for post-save signal on the OrderLineItem model.
# Triggered when an OrderLineItem instance is created or updated.
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the total price of the associated order
    when an order line item is saved.
    This includes both creation and updates of the OrderLineItem.
    """
    # Call the update_total method of the order to recalculate its totals.
    instance.order.update_total()


# Signal (@receiver) listens for post-delete signal on the OrderLineItem model.
# Triggered when an OrderLineItem instance is deleted.
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the total price of the associated order
    when an order line item is deleted.
    """
    # Call the update_total method of the order to recalculate its totals.
    instance.order.update_total()
