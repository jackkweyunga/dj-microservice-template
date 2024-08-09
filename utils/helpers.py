from cargo.models import DriverModel, OrderModel


def check_user_exists(*models, user):
    for model in models:
        if model.objects.filter(user=user).exists():
            return True
