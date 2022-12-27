from datetime import datetime


def timer(name_function):
    def timer_real(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            time = end - start
            print(f"function '{name_function}' execution time: {time.seconds}s, {time.microseconds}ms")
            return result
        return wrapper
    return timer_real
