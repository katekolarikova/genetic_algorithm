import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib; matplotlib.use("TkAgg")

def PrintPlot(current_pop):

    fig = plt.figure()

    x = [current_pop[i].location[0] for i in range(len(current_pop))]
    y = [current_pop[i].location[1] for i in range(len(current_pop))]

    plt.scatter(x, y, marker='o', color='red', label='Města')
    plt.plot(x, y, linestyle='-', color='blue', label='Optimální cesta')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Problém obchodního cestujícího')
    plt.grid(True)
    plt.show()