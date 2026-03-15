from rest_framework import serializers
from .models import ItemRequest


class ItemRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemRequest
        fields = "__all__"
        read_only_fields = ["owner", "created_at"]