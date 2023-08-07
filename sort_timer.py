# Author: Jacob Hensel
# GitHub username: jrh1020
# Date: 8/4/2023
# Description: Uses decorators to add additional behavior to sorting algorithm functions in order to
#              determine and display algorithm performance. Uses matplotlib to graph performance.

import time
import random
import functools
from matplotlib import pyplot

import mergesort
import quicksort
import heapsort
import radixsort
import timsort


def sort_timer(sort_fn: callable) -> callable:
    """
    Decorates a sorting algorithm function to return the elapsed time to run the algorithm

    :param sort_fn: Function handle for a sorting algorithm function (callable)
    :return: Function handle with a decorator for the given function (callable)
    """
    @functools.wraps(sort_fn)
    def wrapper(*args, **kwargs) -> float:

        begin_time = time.perf_counter()  # Get start time
        sort_fn(*args, **kwargs)  # Call the sort function
        end_time = time.perf_counter()  # Get end time

        return end_time - begin_time  # Return elapsed time

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def make_lists_of_sort_times(sort_fns: list[callable], lengths_list: list[int]) -> tuple[list[float], list[float]]:
    """
    Creates random lists of given sizes, calls the sorting algorithms as given to sort the randomized lists, and records
    and returns the elapsed time taken to run the sorting algorithms for each randomized list

    :param sort_fns: List of function handles for sorting algorithms to be tested (callable)
    :param lengths_list: List of sizes of random lists to be generated and tested (list[int])
    :return: A 2-tuple containing the runtimes of the sorting algorithms for each given list length
    """

    time_elapsed_per_size = []

    for size in lengths_list:
        rand_list_master = []
        for i in range(0, size):
            rand_list_master.append(random.randint(1, 10000))

        times_for_this_size = []
        for sort_fn in sort_fns:
            rand_list = list(rand_list_master)
            sort_timer_fn = sort_timer(sort_fn)
            times_for_this_size.append(sort_timer_fn(rand_list))

        time_elapsed_per_size.append(times_for_this_size)

    # Turn each list of times per array size to list of times per sort algorithm
    times = tuple()
    for i in range(len(time_elapsed_per_size[0])):
        time_elapsed_per_fn = []
        for j in range(len(time_elapsed_per_size)):
            time_elapsed_per_fn.append(time_elapsed_per_size[j][i])
        times = times + tuple([time_elapsed_per_fn])

    return times


def compare_sorts(sort_fns: list[callable], lengths_list: list[int]):

    """
    Compares the two given sorting algorithm functions and plots their performances using matplotlib

    :param sort_fns: Function handle for first sorting algorithm to be tested (callable)
    :param lengths_list: List of array lengths to be tested
    """

    # Lists of randomized lists to be generated

    timing_data = make_lists_of_sort_times(sort_fns, lengths_list)  # Get performance data

    # Plot each algorithm's performance and label the plot
    colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']
    for i in range(len(sort_fns)):
        pyplot.plot(lengths_list, timing_data[i], f'{colors[i % 7]}o--', linewidth=2, label=sort_fns[i].__name__)

    # pyplot.yscale('log')
    pyplot.title("Sorting Algorithms: Time to Sort v. List Size")
    pyplot.xlabel("List Size")
    pyplot.ylabel("Elapsed Time (sec)")
    pyplot.legend(loc='upper left')
    pyplot.show()


def main():

    lengths_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 50000, 100000, 250000, 500000, 1000000]
    # lengths_list = [100, 200, 300, 400, 500]  # For smaller test cases

    # compare_sorts([bubble_sort, insertion_sort, quicksort.quick_sort, heapsort.heap_sort, timsort.tim_sort,
    #                radixsort.radix_sort, mergesort.merge_sort], lengths_list)
    # compare_sorts([quicksort.quick_sort, heapsort.heap_sort], lengths_list)
    compare_sorts([quicksort.quick_sort, heapsort.heap_sort, timsort.tim_sort, radixsort.radix_sort,
                   mergesort.merge_sort], lengths_list)


if __name__ == '__main__':
    main()
