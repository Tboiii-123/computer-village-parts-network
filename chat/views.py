from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Conversation
from .serializers import ConversationSerializer,MessageSerializer
from account.models import User


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def start_conversation(request, user_id):

    other_user = get_object_or_404(User, id=user_id)

    conversation = Conversation.objects.filter(
        Q(user1=request.user, user2=other_user) |
        Q(user1=other_user, user2=request.user)
    ).first()

    if conversation:
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)

    conversation = Conversation.objects.create(
        user1=request.user,
        user2=other_user
    )

    serializer = ConversationSerializer(conversation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_message(request, conversation_id):

    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.user not in [conversation.user1, conversation.user2]:
        return Response({"error": "Not allowed"}, status=403)

    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(
            sender=request.user,
            conversation=conversation
        )

        conversation.last_message_time = serializer.instance.created_at
        conversation.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_messages(request, conversation_id):

    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.user not in [conversation.user1, conversation.user2]:
        return Response({"error": "Not allowed"}, status=403)

    messages = conversation.messages.all().order_by("created_at")

    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)




from django.db.models import Q


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_conversations(request):

    conversations = Conversation.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    ).order_by("-last_message_time")

    serializer = ConversationSerializer(conversations, many=True)

    return Response(serializer.data)