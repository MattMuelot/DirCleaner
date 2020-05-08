import datetime


class Decorators:
    @classmethod
    def completion_decorator(cls, func):
        def wrapper(*args, **kwargs):
            with open('directorylog.txt', 'a') as f:
                dir_result = func(*args, **kwargs)
                if not dir_result:
                    f.write(f'ERROR OCCURRED: {datetime.datetime.today()}\n')
                else:
                    f.write(f'{dir_result} FILES MOVED: {datetime.datetime.today()}\n')
        return wrapper
