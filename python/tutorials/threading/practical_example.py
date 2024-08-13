#!/usr/bin/python

from time import perf_counter
from threading import Thread


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the fie
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = [
        './test1.txt',
        './test2.txt',
        './test3.txt',
        './test4.txt',
        './test5.txt',
        './test6.txt',
        './test7.txt',
        './test8.txt',
        './test9.txt',
    ]

    # create threads
    threads = [Thread(target=replace, args=(filename, 'id', 'ids'))
               for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time - start_time: 0.2f} second(s).')
