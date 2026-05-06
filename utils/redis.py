import hashlib
import json
from functools import wraps

from django.core.cache import cache
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)


def cache_response(timeout=60, vary_user=False):
    def decorator(view_func):
        # logger.info("DECORATOR ENTERED")
   
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.method != "GET":
                return view_func(request, *args, **kwargs)

            query_params = request.GET.urlencode()
            user_part = (
                f":user:{request.user.id}"
                if vary_user and getattr(request, "user", None)
                and request.user.is_authenticated
                else ""
            )

            raw_key = f"{request.path}|{query_params}|{user_part}"
            cache_key = "api:" + hashlib.sha256(raw_key.encode()).hexdigest()

            cached_data = cache.get(cache_key)

            if cached_data is not None:
                logger.info(f"[CACHE HIT] {cache_key}")
                return Response(cached_data)

            logger.info(f"[CACHE MISS] {cache_key}")

            response = view_func(request, *args, **kwargs)

            if  response.status_code == 200:
                try:
                      cache.set(cache_key, response.data, timeout)
                      logger.info(f"[CACHE SET] {cache_key}")
                except (TypeError, ValueError):
                    pass  # Don't cache if data isn't serializable

            return response

        return _wrapped_view
    return decorator