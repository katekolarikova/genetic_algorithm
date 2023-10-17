import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib; matplotlib.use("TkAgg")




def PrintPlot(current_pop):

    fig = plt.figure()

    # for current_pop in history_of_best_routes:
    # # Získání seznamu x a y souřadnic měst
    x = [current_pop[i].location[0] for i in range(len(current_pop))]
    y = [current_pop[i].location[1] for i in range(len(current_pop))]
    names = [current_pop[i].name for i in range(len(current_pop))]
    #
    # # Vykreslení jednotlivých bodů
    plt.scatter(x, y, marker='o', color='red', label='Města')
    #
    #     # Vykreslení spojení mezi městy (nejlepší nalezenou cestou)
    #     # best_tour = ["A", "B", "D", "E", "C"]  # Nahraďte svým nejlepším nalezeným řešením
    #     # best_tour_x = [cities[city][0] for city in best_tour]
    #     # best_tour_y = [cities[city][1] for city in best_tour]
    #     # best_tour_x.append(best_tour_x[0])
    #     # best_tour_y.append(best_tour_y[0])  # Přidejte spojení zpět na začátek
    #
    plt.plot(x, y, linestyle='-', color='blue', label='Optimální cesta')
    #
    #     # Popisky jednotlivých bodů (měst)
    #     # for city, (x, y) in cities.items():
    #     #     plt.annotate(city, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # def update_plot(t):
    #     plt.cla()
    #     print(t)
    #     current_pop = history_of_best_routes[t]
    #     x = [current_pop[i].location[0] for i in range(len(current_pop))]
    #     y = [current_pop[i].location[1] for i in range(len(current_pop))]
    #     plt.scatter(x, y, marker='o', color='red', label='Města')
    #     plt.plot(x, y, linestyle='-', color='blue', label='Optimální cesta')
    #
    # num_frames = len(history_of_best_routes)
    # ani = FuncAnimation(fig=fig, func=update_plot, frames=num_frames, interval=100, repeat=False)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Problém obchodního cestujícího')
    plt.grid(True)
    plt.show()