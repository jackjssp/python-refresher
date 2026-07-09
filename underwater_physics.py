import numpy as np
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
    yPos = (T[0] + T[1]) * np.sin(alpha)
    yNeg = (T[2] + T[3]) * np.sin(alpha)
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

testTorque = [12.27, 3.27, 3.8, 5.15]
print(calculate_auv2_angular_acceleration(testTorque, 1.09, 0.516, 0.3, 12.27))