import os
import time
import functools


def terminate():
    if os.name == 'nt':
        import msvcrt
        print("\n\nPress any key to exit...")
        msvcrt.getch()
    else:
        exit()


def time_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Running: {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'"{func.__name__} has finished. \nIt took (approximately) {elapsed_time:.4f}s. ')
        return result
    return wrapper


def prepare(str_):
    return str_.lower().replace(" ", "")


if __name__ == "__main__":
    print("Nothing to see here...")
    terminate()
