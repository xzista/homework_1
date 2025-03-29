from datetime import datetime


def log(filename: str = None):
    def wrapper(func):
        def inner(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_finish = datetime.now()
            text_log_s = f'Функция {func.__name__} запущена: {time_start.strftime("%Y-%m-%d %H:%M:%S")}\n'
            text_log_f = f'Функция {func.__name__} закончила работу: {time_finish.strftime("%Y-%m-%d %H:%M:%S")}\n'
            if not filename:
                print(text_log_s, text_log_f, sep='')
            else:
                print('File')
                with open(filename, 'a', encoding='utf-8') as log_file:
                    log_file.write(text_log_s)
                    log_file.write(text_log_f)
            return result
        return inner
    return wrapper
