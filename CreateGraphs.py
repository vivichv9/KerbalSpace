import numpy as np
import matplotlib.pyplot as plt

def create_graph_cialkovskiy_by_time(gforce, time, rocket_mass, impulse):
    fuel_mass = np.linspace(10000, 0, np.size(gforce))
    gforce += 1
    chast = fuel_mass / rocket_mass
    np.seterr(divide='ignore')
    cialk = (impulse * gforce * np.emath.log(chast))
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(time, cialk, label="Циалковский от времени")
    plt.ylabel("Циаковский")
    plt.xlabel("Время")
    plt.title("Циалковский от времени")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()


def create_graph_velocity_by_mass(mass, velocity):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(mass, velocity, label="Скорость от Массы")
    plt.ylabel("Скорость")
    plt.xlabel("Масса")
    plt.title("Скорость от Массы")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()

def create_graph_velocity_by_time(time, velocity):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(time, velocity, label="Скорость от Времени")
    plt.ylabel("Скорость")
    plt.xlabel("Время")
    plt.title("Скорость от Времени")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()

def create_graph_velocity_by_altitude(altitudeFromTerrain, velocity):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(altitudeFromTerrain, velocity, label="Скорость от высоты")
    plt.ylabel("Скорость")
    plt.xlabel("Высота")
    plt.title("Скорость от высоты")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()

def create_graph_mass_by_time(mass, time):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(time, mass, label="Масса от времени")
    plt.ylabel("Масса")
    plt.xlabel("Время")
    plt.title("Масса от времени")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()

def create_graph_altitude_by_time(time, altitude):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(time, altitude, label="Высота от времени")
    plt.ylabel("Высота")
    plt.xlabel("Время")
    plt.title("Высота от времени")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()

def create_graph_GForce_by_altitude(altitudeFromTerrain, gforce):
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(altitudeFromTerrain, gforce, label="Ускорение свободного падения G от высоты")
    plt.ylabel("Ускорение свободного падения G")
    plt.xlabel("Высота")
    plt.title("Ускорение свободного падения G от высоты")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()


def create_graph_UniversalGravityLaw_by_time(mass_earth, mass_rocket, AFT, time):
    G = 6.67*10**(-11)
    universal_gravity_law = G * ((mass_rocket * mass_earth) / AFT*AFT)
    ax1 = plt.subplot(1, 1, 1)
    plt.plot(time, universal_gravity_law, label="Закон всемирного тяготения от времени")
    plt.ylabel("Закон всемирного тяготения")
    plt.xlabel("время")
    plt.title("Закон всемирного тяготения от времени")
    ax1.grid(color='w', linewidth=0.2)
    plt.show()
