from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import ItemRequest
from .serializers import ItemRequestSerializer


from django.shortcuts import get_object_or_404
#For Pagination
from rest_framework.pagination import PageNumberPagination

#Redis Implementation
from utils.redis import cache_response
from django.core.cache import cache

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_item_request(request):

    serializer = ItemRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(owner=request.user)
        cache.clear() 
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
@permission_classes([IsAuthenticated])
@cache_response(timeout=60, vary_user=False)
def get_all_requests(request):

    item_requests = ItemRequest.objects.filter(status="active").select_related('owner').order_by("-created_at")

    #A paginator controller
    paginator = PageNumberPagination()
    paginator.page_size = 10  # optional (or rely on settings.py)

    paginated_queryset = paginator.paginate_queryset(item_requests, request)
    serializer = ItemRequestSerializer(paginated_queryset, many=True)

   

    
    #Wrapping my reponse in a standard paginator reponse
    return paginator.get_paginated_response(serializer.data)





@api_view(["GET"])
@permission_classes([IsAuthenticated])
#vary_user =False means public if set to true menas personal cache

@cache_response(timeout=60, vary_user=False)
def request_detail(request, request_id):

    item_request = get_object_or_404(ItemRequest, id=request_id)

    serializer = ItemRequestSerializer(item_request)

    return Response(serializer.data)