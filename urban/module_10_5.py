from datetime import datetime
from multiprocessing import Pool


def timing(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(func.__name__, end - start)

    return wrapper


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


@timing
def line_run(lst_files):
    for name_file in lst_files:
        read_info(name_file)


@timing
def multi_run(lst_files):
    with Pool(processes=4) as pool:
        pool.map(read_info, lst_files)


if __name__ == "__main__":
    files = []
    for i in range(1, 5):
        files.append(f"file {i}.txt")

    line_run(files)
    multi_run(files)

