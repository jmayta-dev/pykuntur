"""
Global utils for pykuntur project.
"""
import os


def get_env(var_name: str) -> str:
    """Get the environmennt variable or return exception"""
    from django.core.exceptions import ImproperlyConfigured
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {var_name} environment variable'
        raise ImproperlyConfigured(error_msg)
