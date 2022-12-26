import numpy as np
import matplotlib.pyplot as plt
from parse_data import Columns
from CsvParse import parseCSV
import CreateGraphs

plt.style.use('dark_background')

DATA_FILE_PATH = "data/data.csv"
MASS_EARTH = 5.9722 * 1024

def calculate_impulse(mass, velocity):
    return mass * velocity

Data = parseCSV(DATA_FILE_PATH)

time = np.array(Columns(Data, "Time"))
velocity = np.array(Columns(Data, "Velocity"))
G = np.array(Columns(Data, "Gforce"))
acceleration = np.array(Columns(Data, "Acceleration"))
thrust = np.array(Columns(Data, "Thrust"))
twr = np.array(Columns(Data, "TWR"))
mass = np.array(Columns(Data, "Mass"))
AFT = np.array(Columns(Data, "AltitudeFromTerrain"))
AFS = np.array(Columns(Data, "AltitudeFromSea"))
downrangeDistance = np.array(Columns(Data, "DownrangeDistance"))
latitude = np.array(Columns(Data, "Latitude"))
longitude = np.array(Columns(Data, "Longitude"))
apoapsis = np.array(Columns(Data, "Apoapsis"))
periapsis = np.array(Columns(Data, "Periapsis"))
inclination = np.array(Columns(Data, "Inclination"))
OV = np.array(Columns(Data, "OrbitalVelocity"))
TD = np.array(Columns(Data, "TargetDistance"))
TV = np.array(Columns(Data, "TargetVelocity"))
SDV = np.array(Columns(Data, "StageDeltaV"))
VDV = np.array(Columns(Data, "VesselDeltaV"))
pressure = np.array(Columns(Data, "Pressure"))

CreateGraphs.create_graph_mass_by_time(mass, time)
CreateGraphs.create_graph_velocity_by_time(time, velocity)
CreateGraphs.create_graph_velocity_by_altitude(AFT, velocity)
CreateGraphs.create_graph_velocity_by_mass(mass, velocity)
CreateGraphs.create_graph_altitude_by_time(time, AFT)
CreateGraphs.create_graph_GForce_by_altitude(AFT, G)
CreateGraphs.create_graph_cialkovskiy_by_time(G, time, mass, calculate_impulse(mass, velocity))
CreateGraphs.create_graph_UniversalGravityLaw_by_time(MASS_EARTH, mass, AFT, time)

print(mass[0])