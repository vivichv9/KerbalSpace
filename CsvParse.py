def parseCSV(path):
    s = ""
    Arr = [[]] * 21
    file = open(path, "r")
    s = file.readline()

    while s != "":
        s = file.readline().split(",")
        if len(s) == 1: break
        for i in range(0, 21):
            Arr[i] = Arr[i] + [float(s[i])]
    return Arr
