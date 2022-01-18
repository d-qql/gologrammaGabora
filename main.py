import cmath
import math
import numpy as np
import imageio
lambdaLaser = 600  # нм
lambdaPoint = 600  # нм
dpi = 1000
gologramRad = 10  # мм
z0 = 5  # см

kLaser = 2 * cmath.pi / (lambdaLaser * 1e-9)
kPoint = 2 * cmath.pi / (lambdaPoint * 1e-9)


def waveLaser(z):
    return cmath.exp(1j * kLaser * z)


def wavePoint(x, y, z):
    r = cmath.sqrt(x ** 2 + y ** 2 + z ** 2)
    return cmath.exp(1j * kPoint * r) / r


def interfere():
    length = math.ceil(dpi / 25.4 * 2 * gologramRad)
    picture = np.zeros([length, length])
    step = gologramRad / length * 1e-3
    x = - gologramRad / 2 * 1e-3
    z = z0 * 1e-1
    my_file = open("picture.csv", 'w+')
    my_file.write("x, y, value\n")
    for i in range(length):
        y = - gologramRad / 2 * 1e-3
        for j in range(length):
            picture[i][j] = cmath.polar(waveLaser(z) + wavePoint(x, y, z))[0] ** 2
            # print(cmath.polar(waveLaser(z) + wavePoint(x, y, z))[0])
            my_file.write(str(x) + ", " + str(y) + ", " + str(picture[i][j]) + "\n")
            y += step
        x += step
    my_file.close()
    # print(picture)
    imageio.imwrite("out.png", picture)

if __name__ == "__main__":
    interfere()
