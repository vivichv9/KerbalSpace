def Columns(args, numberOfColumn):
    Arr = args
    numberOfColumn = str(numberOfColumn)
    if (numberOfColumn == "Time"): return Arr[0]
    elif (numberOfColumn == "Velocity"): return Arr[1]
    elif (numberOfColumn == "Gforce"): return Arr[2]
    elif (numberOfColumn == "Acceleration"): return Arr[3]
    elif (numberOfColumn == "Thrust"): return Arr[4]
    elif (numberOfColumn == "TWR"): return Arr[5]
    elif (numberOfColumn == "Mass"): return Arr[6]
    elif (numberOfColumn == "AltitudeFromTerrain"): return Arr[7]
    elif (numberOfColumn == "AltitudeFromSea"): return Arr[8]
    elif (numberOfColumn == "DownrangeDistance"): return Arr[9]
    elif (numberOfColumn == "Latitude"): return Arr[10]
    elif (numberOfColumn == "Longitude"): return Arr[11]
    elif (numberOfColumn == "Apoapsis"): return Arr[12]
    elif (numberOfColumn == "Periapsis"): return Arr[13]
    elif (numberOfColumn == "Inclination"): return Arr[14]
    elif (numberOfColumn == "OrbitalVelocity"): return Arr[15]
    elif (numberOfColumn == "TargetDistance"): return Arr[16]
    elif (numberOfColumn == "TargetVelocity"): return Arr[17]
    elif (numberOfColumn == "StageDeltaV"): return Arr[18]
    elif (numberOfColumn == "VesselDeltaV"): return Arr[19]
    elif (numberOfColumn == "Pressure"): return Arr[20]
    else: return print("non-correct data name")
