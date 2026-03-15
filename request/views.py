from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import ItemRequest
from .serializers import ItemRequestSerializer


from django.shortcuts import get_object_or_404


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_item_request(request):

    serializer = ItemRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_request_status(request, request_id):

    item_request = get_object_or_404(ItemRequest, id=request_id)

    if item_request.owner != request.user:
        return Response(
            {"error": "Not allowed"},
            status=403
        )

    serializer = ItemRequestSerializer(
        item_request,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(["GET"])
def get_all_requests(request):

    requests = ItemRequest.objects.filter(status="active").order_by("-created_at")

    serializer = ItemRequestSerializer(requests, many=True)

    return Response(serializer.data)





@api_view(["GET"])
def request_detail(request, request_id):

    item_request = get_object_or_404(ItemRequest, id=request_id)

    serializer = ItemRequestSerializer(item_request)

    return Response(serializer.data)