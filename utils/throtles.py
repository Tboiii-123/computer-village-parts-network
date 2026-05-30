# throttles.py

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

#AnonRateThrottle for annonymous
#Annon uses IP address cause dey are not authenticated

#UserRateThrottle for authenticated user
#authenticated user ID


class LoginThrottle(AnonRateThrottle):
    rate = "5/min"


class RegisterThrottle(AnonRateThrottle):
    rate = "3/min"


class UserThrottle(UserRateThrottle):
    rate = "15/min"