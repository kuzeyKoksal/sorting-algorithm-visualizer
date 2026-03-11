import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data


def update_plot(data, bars):
    for bar, value in zip(bars, data):
        bar.set_height(value)


def main():
    data = [random.randint(1, 100) for _ in range(15)]

    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")

    bars = ax.bar(range(len(data)), data)

    generator = bubble_sort(data.copy())

    def animate(frame):
        update_plot(frame, bars)

    animation.FuncAnimation(
        fig,
        animate,
        frames=generator,
        repeat=False,
        interval=300
    )

    plt.show()


main()
