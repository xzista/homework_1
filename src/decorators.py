import os
from datetime import datetime
from functools import wraps


def log(filename: str = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            current_dir = os.path.dirname(__file__)  # Папка, где лежит модуль
            log_path = os.path.join(current_dir, "../logs/" + filename)  # Абсолютный путь к файлу
            time_start = datetime.now()
            text_log_s = f'[{time_start.strftime("%Y-%m-%d %H:%M:%S")}] Function {func.__name__} started with inputs: {(*args,)}\n'
            try:
                result = func(*args, **kwargs)
            except ZeroDivisionError as e:
                time_error = datetime.now()
                text_log_e = f'[{time_error.strftime("%Y-%m-%d %H:%M:%S")}] {func.__name__} error: {e}. Inputs: {(*args,)}\n'
                if not filename:
                    print(text_log_s, text_log_e, sep='')
                    raise e
                else:
                    print('FileEr')
                    with open(log_path, 'a', encoding='utf-8') as log_file:
                        log_file.write(text_log_s)
                        log_file.write(text_log_e)
                    raise e
            time_finish = datetime.now()
            text_log_f = f'[{time_finish.strftime("%Y-%m-%d %H:%M:%S")}] Function {func.__name__} finished successfully with result: {result}\n'
            if not filename:
                print(text_log_s, text_log_f, sep='')
            else:
                print('File')
                with open(log_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(text_log_s)
                    log_file.write(text_log_f)
            return result
        return inner
    return wrapper
