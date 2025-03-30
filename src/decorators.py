import os
from datetime import datetime
from functools import wraps


def log(filename: str = ""):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            current_dir = os.path.dirname(__file__)
            log_path = os.path.join(current_dir, "../logs/" + filename)
            time_start = datetime.now()
            text_log_s = (
                f'[{time_start.strftime("%Y-%m-%d %H:%M:%S")}] '
                f"Function {func.__name__} started with inputs: {(*args, ), {**kwargs, }}\n"
            )
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                time_error = datetime.now()
                text_log_e = (
                    f'[{time_error.strftime("%Y-%m-%d %H:%M:%S")}] '
                    f"{func.__name__} error: {e}. Inputs: {(*args, ), {**kwargs, }}\n"
                )
                if not filename:
                    print(text_log_s, text_log_e, sep="", end="")
                    raise e
                else:
                    with open(log_path, "a", encoding="utf-8") as log_file:
                        log_file.write(text_log_s)
                        log_file.write(text_log_e)
                    print("Written in the log file")
                    raise e
            time_finish = datetime.now()
            text_log_f = (
                f'[{time_finish.strftime("%Y-%m-%d %H:%M:%S")}] '
                f"Function {func.__name__} finished successfully with result: {result}\n"
            )
            if not filename:
                print(text_log_s, text_log_f, sep="", end="")
            else:
                with open(log_path, "a", encoding="utf-8") as log_file:
                    log_file.write(text_log_s)
                    log_file.write(text_log_f)
                print("Written in the log file")
            return result

        return inner

    return wrapper
