"""
    Concept: Gravitational Time Dilation

    Parameters Involved:
    M (float): Mass of the massive object (kg)
    r (float): Distance from the center of the massive object 'M' (m)
    G (float): Gravitational constant (m^3 kg^-1 s^-2)
    c (float): Speed of light (m/s)
    delta_t (float): Time interval experienced by a distant observer (s)
    delta_t_prime (float): Time interval experienced by the observer near the Massive Planet (s)

"""

import math

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 2.998e8       # Speed of light (m/s)

# Known Mass and Radius of planets and the Sun of our Solar System.
mass_of_earth = 5.972e24
mass_of_jupiter = 1.8987e27
mass_limit_of_planet = 75 * mass_of_jupiter # https://chandra.harvard.edu/edu/formal/stellar_ev/story/index6.html#:~:text=For%20the%20fusion%20reactions%20to%20occur%2C%20though%2C%20the,8%20percent%20of%20the%20mass%20of%20the%20Sun.
radius_of_earth = 6378.1370 * 1000 # in meters
radius_of_jupiter = 69911000 # in meters
min_radius_of_planet = 300 # in meters. Bodies with radii around 300 to 400 meters or larger are more likely to achieve a nearly round shape, though this can vary based on composition and density.
mass_of_sun = 1.989e30 # in Kg
radius_of_sun = 695700000 # in meters
dist_earth_to_sun = 149597870700 #in meters
One_AU = dist_earth_to_sun

# Radius (in meters) and Mass (in Kg) of Largest Planets in Planetray System (HD 100546) ever found
# Refer: https://astrophotographylens.com/blogs/astro/hd-100546-b-planet
mass_of_HD100546b = 25 * mass_of_jupiter # Protoplanet
radius_of_HD100546b =  482385900 # in meters.
mass_of_HD100546c = 20 * mass_of_jupiter # Potential planetary companion or a more massive object like a brown dwarf.
radius_of_HD100546c =  1.4960e10 # in meters. 

# Maximum radius of a habitable planet is 2.2 times Radius of earth (https://arxiv.org/pdf/1311.3039)
radius_limit_of_habitable_planet = 2.2 * radius_of_earth

# ============================= FUNCTIONS ================================ #

def gravitational_time_dilation(M, r, G, c, delta_t_prime):
    # Calculate the time dilation for the observer far away from the source of gravitational field.
    time_dilation_factor = math.sqrt(1 - ((2 * G * M) / (r * c**2)))
    #print(f" Time Dilation Factor = {time_dilation_factor:.8f} = {time_dilation_factor:.2e}")
    delta_t = delta_t_prime * time_dilation_factor

    return delta_t

def Mass_Per_Radius_GTR(G, c, delta_t_prime, delta_t):
    # Calculate the Mass/Radius Factor:
    mass_per_radius = (c**2 / (2 * G)) * (1 - (delta_t_prime / delta_t)**2)

    return mass_per_radius

# ========================================================================== #

"""
print(f" Mass Limit of Planet before it tuns into a STAR = {mass_limit_of_planet:.6f} = {mass_limit_of_planet:.2e} Kg/m")
print(f" Radius Limit of a Habitable Planet = {radius_limit_of_habitable_planet:.6f} = {radius_limit_of_habitable_planet:.2e} m")

# Calculating the Maximum Time Dilation that can occur from the largest planetary boides in known Universe.
# Time Dilation at HD 100546 b (Protoplanet):
delta_t_prime = 1 # To calculate 1 sec (on HD 100546 b) time dilation. 
time_dilated_HD100546b = gravitational_time_dilation(mass_of_HD100546b, radius_of_HD100546b, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_HD100546b:.12f} secs on HD100546b")

# Time Dilation at HD 100546 c (Almost a Brown Dwarf):
delta_t_prime = 1 # To calculate 1 sec (on HD 100546 c) time dilation. 
time_dilated_HD100546c = gravitational_time_dilation(mass_of_HD100546c, radius_of_HD100546c, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_HD100546c:.12f} secs on HD100546c")

# Calculating the Maximum Time Dilation that can occur from the our planetary boides Earth & Jupiter.
# Time Dilation on Jupiter:
delta_t_prime = 1 # To calculate 1 sec (on Jupiter) time dilation. 
time_dilated_jupiter = gravitational_time_dilation(mass_of_jupiter, radius_of_jupiter, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_jupiter:.12f} secs on Jupiter")

# Time Dilation on Earth due to Earth G-Field:
delta_t_prime = 1 # To calculate 1 sec (on earth) time dilation. 
time_dilated_earth = gravitational_time_dilation(mass_of_earth, radius_of_earth, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_earth:.12f} secs on Earth due to Earth's G-Field")
"""

# Time Dilation on Earth due to Sun's G-Field:
delta_t_prime = 1 # To calculate 1 sec (on earth) time dilation. 
time_dilated_earth = gravitational_time_dilation(mass_of_sun, dist_earth_to_sun, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_earth:.12f} secs on Earth due to Sun's G-Field")
# Calculate the M/R ratio for Time Dilation on Earth due to Sun's G-Field:
mass_per_radius = mass_of_sun / dist_earth_to_sun
print(f" Mass / Radius - Ratio for Sun's G-Field on Earth is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# ================================================================ BRAHMA-MAANA ================================================== #
# Calculate the M/R ratio for Satya-loka and it's STAR:
# Time Relation between Brahma and Manushya 1 sec of Brahma is 3.1104e12 seconds for humans.
delta_t_brahma = 1 # in secs (This is similar to delta_t_prime)
delta_t = time_dilated_earth * 3.1104e12 # in secs
# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_brahma, delta_t)
print(f" Mass / Radius of Satya-loka is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# Calculating the mass of the STAR that Satyaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_satyaloka = mass_per_radius * One_AU
print(f" Mass of the STAR that Satyaloka revolves around in One_AU (As Brahma's One Year is 360 days) is  = {mass_of_star__of_satyaloka:.12f} = {mass_of_star__of_satyaloka:.2e} kg")
if((mass_of_star__of_satyaloka > 1e9 * mass_of_sun) and (mass_of_star__of_satyaloka < 1e11  * mass_of_sun)):
    print(" STAR is a Ultramassive Blackhole")
elif((mass_of_star__of_satyaloka > 1e6 * mass_of_sun) and (mass_of_star__of_satyaloka < 1e9  * mass_of_sun)):
    print(" STAR is a Supermassive Blackhole")
elif((mass_of_star__of_satyaloka > 1e2 * mass_of_sun) and (mass_of_star__of_satyaloka < 1e5  * mass_of_sun)):
    print(" STAR is a Intermediate-mass Blackhole")
elif((mass_of_star__of_satyaloka > 2 * mass_of_sun) and (mass_of_star__of_satyaloka < 150  * mass_of_sun)):
    print(" STAR is a Stellar Blackhole")
else:
    print(" STAR is a Micro Blackhole")
# ================================================================================================================================ #

# ================================================================ MANU-MAANA ================================================== #
# Calculate the M/R ratio for Manu-loka and it's STAR:
# Time Relation between Manu and Manushya 1 sec of Manu is 3067200 seconds for humans.
delta_t_manu = 1 # in secs (This is similar to delta_t_prime)
delta_t = time_dilated_earth * 3067200 # in secs
# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_manu, delta_t)
print(f" Mass / Radius of Manu-loka is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# Calculating the mass of the STAR that Manuloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_manuloka = mass_per_radius * One_AU
print(f" Mass of the STAR that Manuloka revolves around in One_AU (As Manu's One Year is 360 days) is  = {mass_of_star__of_manuloka:.12f} = {mass_of_star__of_manuloka:.2e} kg")
if((mass_of_star__of_manuloka > 1e9 * mass_of_sun) and (mass_of_star__of_manuloka < 1e11  * mass_of_sun)):
    print(" STAR is a Ultramassive Blackhole")
elif((mass_of_star__of_manuloka > 1e6 * mass_of_sun) and (mass_of_star__of_manuloka < 1e9  * mass_of_sun)):
    print(" STAR is a Supermassive Blackhole")
elif((mass_of_star__of_manuloka > 1e2 * mass_of_sun) and (mass_of_star__of_manuloka < 1e5  * mass_of_sun)):
    print(" STAR is a Intermediate-mass Blackhole")
elif((mass_of_star__of_manuloka > 2 * mass_of_sun) and (mass_of_star__of_manuloka < 150  * mass_of_sun)):
    print(" STAR is a Stellar Blackhole")
else:
    print(" STAR is a Micro Blackhole")
# ================================================================================================================================ #

# ================================================================ DEVA-MAANA ================================================== #
# Calculate the M/R ratio for Deva-loka and it's STAR:
# Time Relation between Deva and Manushya 1 sec of Deva is 360 seconds for humans.
delta_t_deva = 1 # in secs (This is similar to delta_t_prime)
delta_t = time_dilated_earth * 360 # in secs
# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_deva, delta_t)
print(f" Mass / Radius of Deva-loka is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# Calculating the mass of the STAR that Satyaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_devaloka = mass_per_radius * One_AU
print(f" Mass of the STAR that Devaloka revolves around in One_AU (As Deva's One Year is 360 days) is  = {mass_of_star__of_devaloka:.12f} = {mass_of_star__of_devaloka:.2e} kg")
if((mass_of_star__of_devaloka > 1e9 * mass_of_sun) and (mass_of_star__of_devaloka < 1e11  * mass_of_sun)):
    print(" STAR is a Ultramassive Blackhole")
elif((mass_of_star__of_devaloka > 1e6 * mass_of_sun) and (mass_of_star__of_devaloka < 1e9  * mass_of_sun)):
    print(" STAR is a Supermassive Blackhole")
elif((mass_of_star__of_devaloka > 1e2 * mass_of_sun) and (mass_of_star__of_devaloka < 1e5  * mass_of_sun)):
    print(" STAR is a Intermediate-mass Blackhole")
elif((mass_of_star__of_devaloka > 2 * mass_of_sun) and (mass_of_star__of_devaloka < 150  * mass_of_sun)):
    print(" STAR is a Stellar Blackhole")
else:
    print(" STAR is a Micro Blackhole")
# ================================================================================================================================ #

# ================================================================ PITRU-MAANA ================================================== #
# Calculate the M/R ratio for Pitru-loka and it's STAR:
# Time Relation between Pitru and Manushya 1 sec of Pitru is 30 seconds for humans.
delta_t_pitru = 1 # in secs (This is similar to delta_t_prime)
delta_t = time_dilated_earth * 30 # in secs
# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_pitru, delta_t)
print(f" Mass / Radius of Pitru-loka is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# Calculating the mass of the STAR that Devaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_pitruloka = mass_per_radius * One_AU
print(f" Mass of the STAR that Pitruloka revolves around in One_AU (As Pitru's One Year is 360 days) is  = {mass_of_star__of_pitruloka:.12f} = {mass_of_star__of_pitruloka:.2e} kg")
if((mass_of_star__of_pitruloka > 1e9 * mass_of_sun) and (mass_of_star__of_pitruloka < 1e11  * mass_of_sun)):
    print(" STAR is a Ultramassive Blackhole")
elif((mass_of_star__of_pitruloka > 1e6 * mass_of_sun) and (mass_of_star__of_pitruloka < 1e9  * mass_of_sun)):
    print(" STAR is a Supermassive Blackhole")
elif((mass_of_star__of_pitruloka > 1e2 * mass_of_sun) and (mass_of_star__of_pitruloka < 1e5  * mass_of_sun)):
    print(" STAR is a Intermediate-mass Blackhole")
elif((mass_of_star__of_pitruloka > 2 * mass_of_sun) and (mass_of_star__of_pitruloka < 150  * mass_of_sun)):
    print(" STAR is a Stellar Blackhole")
else:
    print(" STAR is a Micro Blackhole")
# ================================================================================================================================ #
