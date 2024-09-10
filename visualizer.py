import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# bubble sorting

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

# selection sorting

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

#insertion sorting

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

# merge sorting

def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(arr, start, mid)
        yield from merge_sort(arr, mid, end)
        yield from merge(arr, start, mid, end)
        yield arr

def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    for k in range(start, end):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        yield arr

# quick sorting        

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        yield from quick_sort(arr, low, p)
        yield from quick_sort(arr, p + 1, high)
    yield arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# created this fucntion for the visualization

def visualize_sorting(arr, algorithm):
    fig, ax = plt.subplots()
    ax.set_title(f"Visualizing {algorithm.__name__}")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

# so basically this function is for the animation of the graph by the matplotlib
    def update_plot(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iterations: {iteration[0]}")

    anim = FuncAnimation(fig, func=update_plot, fargs=(bar_rects, iteration),
                         frames=algorithm(arr.copy()), interval=100,
                         repeat=False)

    plt.show()

