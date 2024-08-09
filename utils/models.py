import logging
from functools import partial

from charidfield import CharIDField
from cuid2.generator import Cuid
from django.http import QueryDict
from rest_framework import serializers


def cuid_default_value():
    return Cuid(length=32).generate()


logger = logging.getLogger("django")

CuidField = partial(
    CharIDField,
    default=cuid_default_value,
    max_length=225,
    help_text="cuid-format identifier for this entity."
)


class UserAwareModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes the user from the context and adds it to the
    validated data.
    """

    userinfo = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # check if data is passed in args
        if "data" in kwargs:
            print("data in kwargs", kwargs["data"])
            initial_data = kwargs["data"].copy()
            initial_data["user"] = self.context["request"].user.pk
            self.initial_data = initial_data

    def get_userinfo(self, obj):

        # get the value of user field
        user = obj.user

        # TODO Add more ways to obtain the user associated with the object

        if user:
            return {
                "email": user.email,
                "username": user.username
            }

        return None

