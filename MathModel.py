import numpy as np
import matplotlib.pyplot as plt
import math

time = 240
timeStage1 = 74
timeStage2 = 172
timeStage3 = 240
times = [x for x in range(1, time + 1)]

arrVx = [0]
arrX = [0]
arrY = [0]
arrVy = [0]
arrMass = [0]

E = 2.71828  # Экспонента
G = 9.81  # ускорение свободного падения

K1 = 0.4  # коэффицент лобового сопротивления

K2_STAGE1 = 2000
K2_STAGE2 = 0  # Скорость истечения газа
K2_STAGE3 = 2000

K3_STAGE1 = 340
K3_STAGE3 = 130  # Скорость уменьшения массы
K3_STAGE2 = 0

M = 37400  # масса корабля
alpha = 0
dt = 1

for i in range(1, timeStage1):

    # координата по x
    x1 = arrX[i - 1]
    # скорость по x
    vx1 = arrVx[i - 1]
    K1 *= 0.997
    vx2 = (vx1 + (-math.sin(alpha) * (K1 / M) * vx1 ** 2 + math.sin(alpha) * (K2_STAGE1 * K3_STAGE1) / M) * dt)
    x2 = x1 + vx2 * dt

    y1 = arrY[i - 1]  # координата по x
    vy1 = arrVy[i - 1]  # скорость по x
    vy2 = (vy1 + (-G - math.cos(alpha) * (K1 / M) * vy1 ** 2 + math.cos(alpha) * (K2_STAGE1 * K3_STAGE1) / M) * dt)
    y2 = y1 + vy2 * dt

    alpha += math.pi / (2 * time)

    # масса корабля
    M -= K3_STAGE1 * dt

    arrVx.append(vx2)
    arrX.append(x2)
    arrVy.append(vy2)
    arrY.append(y2)
    arrMass.append(M)

for i in range(timeStage1, timeStage2):
    # координата по x
    x1 = arrX[i - 1]
    # скорость по x
    vx1 = arrVx[i - 1]
    K1 = 0.01
    # скорость ракеты в следующий момент времени
    vx2 = (vx1 + (-math.sin(alpha) * (K1 / M) * vx1 ** 2 + math.sin(alpha) * (K2_STAGE2 * K3_STAGE2) / M) * dt)
    # координата ракеты в следующий момент времени
    x2 = x1 + vx2 * dt

    # координата по x
    y1 = arrY[i - 1]
    # скорость по x
    vy1 = arrVy[i - 1]
    vy2 = (vy1 + (-G - math.cos(alpha) * (K1 / M) * vy1 ** 2 + math.cos(alpha) * (K2_STAGE1 * K3_STAGE2) / M) * dt)
    y2 = y1 + vy2 * dt

    alpha += math.pi / (2 * 240)

    # масса корабля
    M -= K3_STAGE2 * dt

    arrVx.append(vx2)
    arrX.append(x2)
    arrVy.append(vy2)
    arrY.append(y2)
    arrMass.append(M)

for i in range(timeStage2, timeStage3):
    # координата по x
    x1 = arrX[i - 1]
    # скорость по x
    vx1 = arrVx[i - 1]
    K1 = 0
    vx2 = (vx1 + (-math.sin(alpha) * (K1 / M) * vx1 ** 2 + math.sin(alpha) * (K2_STAGE3 * K3_STAGE3) / M) * dt)
    x2 = x1 + vx2 * dt

    # координата по x
    y1 = arrY[i - 1]
    # скорость по x
    vy1 = arrVy[i - 1]
    vy2 = (vy1 + (-G - math.cos(alpha) * (K1 / M) * vy1 ** 2 + math.cos(alpha) * (K2_STAGE3 * K3_STAGE3) / M) * dt)
    y2 = y1 + vy2 * dt

    alpha += math.pi / (2 * 240)

    # масса корабля в следующий момент времени
    M -= K3_STAGE3 * dt
    arrVx.append(vx2)
    arrX.append(x2)
    arrVy.append(vy2)
    arrY.append(y2)
    arrMass.append(M)


times1 = np.asarray(times)
arrayVX = np.asarray(arrVx)
arrayVY = np.asarray(arrVy)
arrayX = np.asarray(arrX)
arrayY = np.asarray(arrY)
arrayMass = np.asarray(arrMass)

sumArrays = np.sqrt(arrayVX * arrayVX + arrayVY * arrayVY)

ax3 = plt.subplot(1, 1, 1)
plt.plot(times1, arrayMass)
plt.ylabel("Масса")
plt.xlabel("Время")
plt.show()

ax4 = plt.subplot(1, 1, 1)
plt.plot(arrayX, arrayY)
plt.ylabel("Координаты по Y")
plt.xlabel("Координаты по X")
plt.show()

ax5 = plt.subplot(1, 1, 1)
plt.plot(times1, sumArrays)
plt.ylabel("Скорость(Вектор)")
plt.xlabel("Время")
plt.show()
