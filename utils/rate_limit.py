def get_client_ip(request):
    """
    Returns the real client IP address.
    Works with proxies if X-Forwarded-For is set.
    Fallbacks to REMOTE_ADDR if X-Forwarded-For is not available.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # X-Forwarded-For can be a comma-separated list; client IP is the first one
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR", "unknown")
    return ip
