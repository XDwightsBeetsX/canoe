import numpy as np
from matplotlib import pyplot as plt


name = "[paddle_stroke]"


def getA(s, paddle_angle=12):
    """
    default paddle_angle of 20deg
    """
    return np.sin(np.pi * s**2) * (180/np.pi) - paddle_angle

def getF(s):
    return np.sin(np.pi * s - np.sin(np.pi * s)) * 100


if __name__ == "__main__":
    print(name + " - starting...")

    # paddle angle start/stop
    angle_start = -20
    angle_end   = 40

    # paddle stroke stages
    catch = 0.4
    power = 0.95

    # ~resolution
    n = 100

    stages = np.arange(0, 1, 1/n)
    shared_x = np.array(stages)
    paddle_angles = []
    forces = []
    applied = []

    print(name + " - getting model values...")
    for s in stages:
        a = getA(s)
        f = getF(s)

        paddle_angles.append(a)
        app = np.cos(a * (np.pi / 180)) * f
        forces.append(f)
        applied.append(app)
    
    # plotting
    print(name + " - plotting...")
    fig, ax1 = plt.subplots()
    
    ax2 = ax1.twinx()
    ax1.set_xlabel("Paddle Stroke")
    
    ax1.set_ylabel("Paddle Angle")
    ax1.plot(stages, paddle_angles, label="Paddle Angle", color='g', linestyle='--')

    ax2.set_ylabel("Force %")
    ax2.plot(stages, forces, label="Force %", color='b', linestyle='-.')
    ax2.plot(stages, applied, label="Applied", color='r', linestyle='-')

    xcoords = [catch, power]
    for xc in xcoords:
        plt.axvline(x=xc, color='k', linestyle='--')
    
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    plt.show()

    print(name + " - done.")
