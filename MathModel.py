import numpy as np
import matplotlib.pyplot as plt
import math

times = [x for x in range(1, 121)]
E = 2.71828  # Экспонента
arrVx = [0]
arrX = [0]
arrY = [0]
arrVy = [0]
arrMass = [0]
dt = 1
G = 9.81  # уск своб падения
K1 = 0.4  # коэффицент лобового сопротивления
K3 = 800  # Скорость уменьшения массы
K2_STAGE1 = 4000  # Скорость истечения газа
K2_STAGE2 = 6000
M = 10**5  # масса корабля
alpha = 0

for i in range(1, 61):

    x1 = arrX[i - 1]  # координата по x
    vx1 = arrVx[i - 1]  # скорость по x
#   vx2 = (vx1 + (-G - (K1 / M) * vx1 ** 2 + (K2 * K3) / M) * dt)
    vx2 = (vx1 + (-math.sin(alpha) * (K1 / M) * vx1 ** 2 + math.sin(alpha) * (K2_STAGE1 * K3) / M) * dt)
    x2 = x1 + vx2 * dt

    y1 = arrY[i - 1]  # координата по x
    vy1 = arrVy[i - 1]  # скорость по x
#   vy2 = (vy1 + (-(K1 / M) * vy1 ** 2 + (K2 * K3) / M) * dt)
    vy2 = (vy1 + (-G - math.cos(alpha) * (K1 / M) * vy1 ** 2 + math.cos(alpha) * (K2_STAGE1 * K3) / M) * dt)
    y2 = y1 + vy2 * dt

    alpha += math.pi / (2 * 120)

    M -= K3 * dt  # масса корабля

    arrVx.append(vx2)
    arrX.append(x2)
    arrVy.append(vy2)
    arrY.append(y2)
    arrMass.append(M)

for i in range(61, 120):
    x1 = arrX[i - 1]  # координата по x
    vx1 = arrVx[i - 1]  # скорость по x
    #   vx2 = (vx1 + (-G - (K1 / M) * vx1 ** 2 + (K2 * K3) / M) * dt)
    vx2 = (vx1 + (-math.sin(alpha) * (K1 / M) * vx1 ** 2 + math.sin(alpha) * (K2_STAGE2 * K3) / M) * dt)
    x2 = x1 + vx2 * dt

    y1 = arrY[i - 1]  # координата по x
    vy1 = arrVy[i - 1]  # скорость по x
    #   vy2 = (vy1 + (-(K1 / M) * vy1 ** 2 + (K2 * K3) / M) * dt)
    vy2 = (vy1 + (-G -math.cos(alpha) * (K1 / M) * vy1 ** 2 + math.cos(alpha) * (K2_STAGE2 * K3) / M) * dt)
    y2 = y1 + vy2 * dt

    alpha += math.pi / (2 * 120)

    M -= K3 * dt  # масса корабля
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

ax1 = plt.subplot(1, 1, 1)
plt.plot(times1, arrayVX)
plt.plot(times1, arrayVY)
plt.show()

ax2 = plt.subplot(1, 1, 1)
plt.plot(times1, arrayX)
plt.plot(times1, arrayY)
plt.show()

ax3 = plt.subplot(1, 1, 1)
plt.plot(times1, arrayMass)
plt.show()

ax4 = plt.subplot(1, 1, 1)
plt.plot(arrayX, arrayY)
plt.show()
