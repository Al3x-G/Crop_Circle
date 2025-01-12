from django.http import HttpResponse


class StripeWH_Handler:
    """Class to handle Stripe webhooks"""

    def __init__(self, request):
        """
        Initialise the handler with the HTTP request object.
        Args:
            request (HttpRequest): The HTTP request
            containing the webhook data.
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a webhook event.
        Args:
            event (dict): The event payload received from Stripe.
        Returns:
            HttpResponse: A response with a message indicating
            the event type and a status code of 200.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
