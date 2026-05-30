from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import ItemResponse
from .serializers import ItemResponseSerializer
from request.models import ItemRequest


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def i_have_it(request, request_id):

    item_request = get_object_or_404(ItemRequest, id=request_id)

    if item_request.owner == request.user:
        return Response(
            {"error": "You cannot respond to your own request"},
            status=status.HTTP_400_BAD_REQUEST
        )

    response, created = ItemResponse.objects.get_or_create(
        request=item_request,
        responder=request.user
    )

    serializer = ItemResponseSerializer(response)

    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(["GET"])
def request_responses(request, request_id):

    responses = ItemResponse.objects.filter(request_id=request_id).select_related("responder").order_by('-created_at')

    serializer = ItemResponseSerializer(responses, many=True)

    return Response(serializer.data)