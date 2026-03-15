from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import UserReport
from .serializers import UserReportSerializer
from account.models import User


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def report_user(request, user_id):
    reported_user = User.objects.filter(id=user_id).first()
    if not reported_user:
        return Response({"error": "User not found"}, status=404)

    # Prevent self-report
    if reported_user == request.user:
        return Response({"error": "You cannot report yourself"}, status=400)

    # Create report
    serializer = UserReportSerializer(data=request.data)
    if serializer.is_valid():
        activity_type = serializer.validated_data.get("activity_type", "other")

        # Check if report already exists
        existing_report = UserReport.objects.filter(
            reported_user=reported_user,
            reported_by=request.user,
            activity_type=activity_type
        ).first()

        if existing_report:
            return Response(
                {"detail": "You have already reported this activity for this user."},
                status=400
            )

        # Save new report
        serializer.save(reported_by=request.user, reported_user=reported_user)

        # Update report count
        reported_user.report_count += 1

        # Suspension logic
        if reported_user.report_count >= 10:
            reported_user.is_suspended = True
        elif reported_user.report_count >= 5:
            # Optionally send a warning
            print(f"Warning: {reported_user.username} has 5+ reports")

        reported_user.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)