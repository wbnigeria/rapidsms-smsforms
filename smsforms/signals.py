from django.dispatch import Signal

form_complete = Signal(providing_args=["session", "form"])