from rest_framework import serializers
from .models import ItemResponse


class ItemResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemResponse
        fields = "__all__"
        read_only_fields = ["responder", "created_at"]