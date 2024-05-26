"""Set of decorators for contacts bot"""
from functools import wraps


def input_error_catch(func):
    """catch input error decorator"""
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f"Value Error: {str(error)}"
        except KeyError as error:
            return f"Key Error: {str(error)}"

    return inner


def require_n_args(n):
    """check amount of args decorator"""
    def decorator(func):
        @wraps(func)
        def inner(args, contacts):
            if len(args) != n:
                raise ValueError(f'Operation Requires {n} args')
            return func(args, contacts)

        return inner
    return decorator


def require_more_eq_n_args(n):
    """check amount of args decorator"""
    def decorator(func):
        @wraps(func)
        def inner(args, contacts):
            if len(args) < 2:
                raise ValueError('Operation Requires 2 args')
            elif len(args) < 4:
                raise ValueError('Address must consist of at least 3 parts')

            return func(args, contacts)

        return inner
    return decorator


def name_min_length(func):
    """check name min length decorator"""
    @wraps(func)
    def inner(args, contacts):
        if len(args[0]) <= 3:
            raise ValueError('Name should be more the 3 symbols')
        return func(args, contacts)

    return inner
