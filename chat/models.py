from django.db import models
from django.conf import settings

from account.models import User


class Conversation(models.Model):

    user1 = models.ForeignKey(
        User,
        related_name="conversations_as_user1",
        on_delete=models.CASCADE
    )

    user2 = models.ForeignKey(
        User,
        related_name="conversations_as_user2",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    last_message_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Conversation between {self.user1} and {self.user2}"


class Message(models.Model):

    conversation = models.ForeignKey(
        Conversation,
        related_name="messages",
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender}"