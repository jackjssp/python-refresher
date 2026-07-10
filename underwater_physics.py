import numpy as np
import turtle as turt
import time
g = 9.81 #m/s

def calculate_buoyancy(Vsub, density_fluid):
    return density_fluid * Vsub * g

def will_it_float(Vtotal, mass): 
    density = mass / Vtotal
    if(density > 1000):
        return False
    else:
        return True

def calculate_pressure(depth):
    return 1000 * g * depth 

def calculate_acceleration(Force, mass):
    return Force / mass

def calculate_angular_acceleratoins(tau, I):
    return tau / I

def calculate_torque(F_magnitude, F_direction, r):
    return F_magnitude*r*np.sin(F_direction)

def calculate_moment_of_inertia(m, r):
    return m * (r**2)

def calculate_auv_acceleration(F_magnitude, F_angle, mass, thruster_distance):
    return (F_magnitude * np.cos(F_angle)) / mass

def calculate_auv_angular_acceleration(F_magnitude, F_angle, I, thruster_distance):
    return (F_magnitude*thruster_distance*np.sin(F_angle)) / I

def calculate_auv2_acceleration(T, alpha, theta, mass):
    xPos = (T[0] + T[1]) * np.cos(alpha)
    xNeg = (T[2] + T[3]) * np.cos(alpha)
    yPos = (T[0] + T[3]) * np.sin(alpha)
    yNeg = (T[1] + T[2]) * np.sin(alpha)
    #print(f"{xPos}, {xNeg}, {yPos}, {yNeg}") #commented print statements are for testing purposes

    xRel = xPos - xNeg
    yRel = yPos - yNeg
    #print(f"{xRel}, {yRel}")

    xFin = xRel * np.cos(theta) - yRel * np.sin(theta)
    yFin = xRel * np.sin(theta) + yRel * np.cos(theta)
    #print(f"{xFin}, {yFin}")
    #print(f"{mass}")

    ax = xFin / mass
    ay = yFin / mass
    #print(f"{ax}, {ay}")

    return [ax, ay]

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    r = np.sqrt((L**2)+(l**2))
    theta = ((np.pi / 2) - alpha) + np.arctan(L/l)
    #print(f"{r}, {theta}")
    torquePos = (T[0] + T[2]) * r * np.sin(theta)
    torqueNeg = (T[1] + T[3]) * r * np.sin(theta)
    torqueNet = torquePos - torqueNeg
    #print(f"{torqueNet}, {torquePos}, {torqueNeg}") #For testing purposes

    return torqueNet / inertia


def simulate_auv2_motion(T, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0):
    accelerationLinear = calculate_auv2_acceleration(T, alpha, theta0, mass)
    accelerationAngular = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)

    t = [0]
    x = [x0]
    y = [y0]
    theta = [theta0]
    v = [[0, 0]]
    omega = [0]
    a = [accelerationLinear]

    tLoop = 0
    counter = 0
    while (tLoop < t_final):
        tLoop += dt
        t.append(tLoop)
        omega.append(accelerationAngular * tLoop)
        theta.append(0.5 * accelerationAngular * (tLoop ** 2))

        x.append(x[counter] + (v[counter][0] * dt) + (0.5 * a[counter][0] * (dt ** 2)))
        y.append(y[counter] + (v[counter][1] * dt) + (0.5 * a[counter][1] * (dt ** 2)))

        v.append([v[counter][0] + (a[counter][0] * dt), v[counter][1] + (a[counter][1] * dt)])
        a.append(calculate_auv2_acceleration(T, alpha, theta[counter + 1], mass))

        counter += 1

    output = [t, x, y, v, theta, omega, a]
    return output

def test_auv2_motion(t, x, y, v, theta, omega, a):
    counter = 0
    screen = turt.Screen()
    turt.pendown()
    for dt in t:
        turt.setheading(theta[0])
        turt.goto(x[counter], y[counter])
        turt.update()
        time.sleep(dt)
        counter += 1


testTorque = [12.3, 32.5, 20, 8.4]
i = simulate_auv2_motion(testTorque, np.pi/4, 0.5, 0.3, 15, 22, 0.1, 10, 0, 0, np.pi/2)
test_auv2_motion(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
#calculate_auv2_angular_acceleration(testTorque, np.pi/4, 0.5, 0.3, 12.27)