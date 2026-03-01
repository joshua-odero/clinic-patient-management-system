def role_required(role):
    """
    Decorator to restrict access based on user role.
    """

    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role != role:
                print("Access denied.")
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator