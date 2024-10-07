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
print(f" Radius Limit of a Habitable Planet = {radius_limit_of_habitable_planet:.6f} = {radius_limit_of_habitable_planet:.2e} m")
# Mass Limit of Planet before it tuns into a STAR. (Refer: https://chandra.harvard.edu/edu/formal/stellar_ev/story/index6.html#:~:text=For%20the%20fusion%20reactions%20to%20occur%2C%20though%2C%20the,8%20percent%20of%20the%20mass%20of%20the%20Sun)
mass_limit_of_planet = 75 * mass_of_jupiter
print(f" Mass Limit of Planet before it tuns into a STAR = {mass_limit_of_planet:.6f} = {mass_limit_of_planet:.2e} Kg/m")

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

# Calculating the Maximum Time Dilation that can occur from the largest planetary boides in known Universe.

# Time Dilation at HD 100546 b (Protoplanet):
delta_t_prime = 1 # To calculate 1 sec (on HD 100546 b) time dilation. 
time_dilated_HD100546b = gravitational_time_dilation(mass_of_HD100546b, radius_of_HD100546b, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_HD100546b:.12f} secs on HD100546b")

# Time Dilation at HD 100546 c (Almost a Brown Dwarf):
delta_t_prime = 1 # To calculate 1 sec (on HD 100546 c) time dilation. 
time_dilated_HD100546c = gravitational_time_dilation(mass_of_HD100546c, radius_of_HD100546c, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_HD100546c:.12f} secs on HD100546c")

# ========================================================================== #

# Calculating the Maximum Time Dilation that can occur from the our planetary boides Earth & Jupiter.

# Time Dilation on Jupiter:
delta_t_prime = 1 # To calculate 1 sec (on Jupiter) time dilation. 
time_dilated_jupiter = gravitational_time_dilation(mass_of_jupiter, radius_of_jupiter, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_jupiter:.12f} secs on Jupiter")

# Time Dilation on Earth due to Earth G-Field:
delta_t_prime = 1 # To calculate 1 sec (on earth) time dilation. 
time_dilated_earth = gravitational_time_dilation(mass_of_earth, radius_of_earth, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_earth:.12f} secs on Earth due to Earth's G-Field")

# ========================================================================== #

# ================================================================ BHU-MAANA ================================================== #
print("# ================================================================ BHU-MAANA ================================================== #")

# Time Dilation on Earth due to Sun's G-Field:
delta_t_prime = 1 # To calculate 1 sec (on earth) time dilation. 
time_dilated_earth = gravitational_time_dilation(mass_of_sun, dist_earth_to_sun, G, c, delta_t_prime)
print(f" A second in Outer Space is = {time_dilated_earth:.12f} secs on Earth due to Sun's G-Field")

# Calculate the M/R ratio for Time Dilation on Earth due to Sun's G-Field:
mass_per_radius = mass_of_sun / dist_earth_to_sun
print(f" Mass / Radius - Ratio for Sun's G-Field on Earth is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# M / R Ratio Calculation according to GTR:
mass_per_radius = Mass_Per_Radius_GTR(G, c, time_dilated_earth, delta_t_prime)
print(f" Mass / Radius of Earth-Sun System is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")

# Orbital Distance (in AU) assuming a circular orbit is calculated as:
T = 1 #in Earth years
orbital_dist_earth = math.pow(T, 2/3)
print(f" Orbital Radius of Earth is = {orbital_dist_earth:.6f} = {orbital_dist_earth:.2e} AU")
if(orbital_dist_earth == 1):
    orbital_dist_earth = One_AU
    print(f" Orbital Radius of Earth is = 1 AU")

# Orbital Distance (in METERS) assuming a circular orbit is calculated as:
T = 31104000 # in seconds (360 days)
orbital_dist_earth = math.sqrt((G * T * T * mass_per_radius) / (4 * math.pi * math.pi))
print(f" Orbital Radius of Earth is = {orbital_dist_earth:.6f} = {orbital_dist_earth:.2e} meters...")

# Calculating the mass of the STAR that Satyaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_sun = mass_per_radius * orbital_dist_earth
print(f" SOLAR MASS  = {mass_of_star__of_sun:.12f} = {mass_of_star__of_sun:.2e} kg")

# Calculating Schwarzchild Radius of the star - SUN:
schwarzchild_rad_of_sun = (2 * G * mass_of_star__of_sun) / (c**2)
print(f" Schwarzchild Radius of the star is = {schwarzchild_rad_of_sun:.6f} = {schwarzchild_rad_of_sun:.2e} meters...")

# ================================================================ BRAHMA-MAANA ================================================== #
print("# ================================================================ BRAHMA-MAANA ================================================== #")

# Calculate the M/R ratio for Satya-loka and it's STAR:
# Time Relation between Brahma and Manushya 1 sec of Brahma is 3.1104e12 seconds for humans.
delta_t_brahma = 1 # in secs (This is similar to delta_t_prime)
delta_t = 3.1104e12 # in secs. This is including the effect of Sun's G-Field on Earth.
T = 31104000 # in secs (acc to Brahma-Maana). 360 days of Brahma is Time period of the planet of Brahma.

# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_brahma, delta_t)
print(f" Mass / Radius of Satya-loka-STAR System is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")
# Orbital Distance assuming a circular orbit is calculated as:
orbital_dist_brahma = math.sqrt((G * T * T * mass_per_radius) / (4 * math.pi * math.pi))
print(f" Orbital Radius of Satya-loka is = {orbital_dist_brahma:.6f} = {orbital_dist_brahma:.2e} m")

# Calculating the mass of the STAR that Satyaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_satyaloka = mass_per_radius * orbital_dist_brahma
print(f" Mass of the STAR that Satyaloka revolves around in Brahma's One Year i.e. 360 days is  = {mass_of_star__of_satyaloka:.12f} = {mass_of_star__of_satyaloka:.2e} kg")

# Calculating Schwarzchild Radius of the star
schwarzchild_rad_of_satyaloka = (2 * G * mass_of_star__of_satyaloka) / (c**2)
print(f" Schwarzchild Radius of the star is = {schwarzchild_rad_of_satyaloka:.6f} = {schwarzchild_rad_of_satyaloka:.2e} meters...")

# Check if Schwarzchild Radius of the star = Orbital Radius of Satyaloka.
if(orbital_dist_brahma == schwarzchild_rad_of_satyaloka):
    print(" Schwarzchild Radius of the Satya-star = Orbital Radius of Satyaloka")
else:
    schwarzchild_orbital_dist_diff_satya = orbital_dist_brahma - schwarzchild_rad_of_satyaloka
    if(schwarzchild_orbital_dist_diff_satya > 0):
        print(f" Orbital Radius of Satyaloka > Schwarzchild Radius of the Satya-star by {schwarzchild_orbital_dist_diff_satya:.6f} m")
    else:
        print(f" Orbital Radius of Satyaloka < Schwarzchild Radius of the Satya-star by {schwarzchild_orbital_dist_diff_satya:.6f} m")

# ================================================================================================================================ #

# ================================================================ MANU-MAANA ================================================== #
print("# ================================================================ MANU-MAANA ================================================== #")

# Calculate the M/R ratio for Manu-loka and it's STAR:
# Time Relation between Manu and Manushya 1 sec of Manu is 3067200 seconds for humans.
delta_t_manu = 1 # in secs (This is similar to delta_t_prime)
delta_t = 3067200 # in secs. This is including the effect of Sun's G-Field on Earth.
T = 31104000 # in secs (acc to Manu-Maana). 360 days of Manu is Time period of the planet of Manu.

# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_manu, delta_t)
print(f" Mass / Radius of Manu-loka-STAR System is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")
# Orbital Distance assuming a circular orbit is calculated as:
orbital_dist_manu = math.sqrt((G * T * T * mass_per_radius) / (4 * math.pi * math.pi))
print(f" Orbital Radius of Manu-loka is = {orbital_dist_manu:.6f} = {orbital_dist_manu:.2e} m")

# Calculating the mass of the STAR that Manuloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_manuloka = mass_per_radius * orbital_dist_manu
print(f" Mass of the STAR that Manuloka revolves around in Manu's One Year i.e. 360 days is  = {mass_of_star__of_manuloka:.12f} = {mass_of_star__of_manuloka:.2e} kg")

# Calculating Schwarzchild Radius of the star
schwarzchild_rad_of_manuloka = (2 * G * mass_of_star__of_manuloka) / (c**2)
print(f" Schwarzchild Radius of the star is = {schwarzchild_rad_of_manuloka:.6f} = {schwarzchild_rad_of_manuloka:.2e} meters...")

# Check if Schwarzchild Radius of the star = Orbital Radius of Manuloka.
if(orbital_dist_manu == schwarzchild_rad_of_manuloka):
    print("Schwarzchild Radius of the Manu-star = Orbital Radius of Manuloka")
else:
    schwarzchild_orbital_dist_diff_manu = orbital_dist_manu - schwarzchild_rad_of_manuloka
    if(schwarzchild_orbital_dist_diff_manu > 0):
        print(f" Orbital Radius of Manuloka > Schwarzchild Radius of the Manu-star by {schwarzchild_orbital_dist_diff_manu:.6f} m")
    else:
        print(f" Orbital Radius of Manuloka < Schwarzchild Radius of the Manu-star by {schwarzchild_orbital_dist_diff_manu:.6f} m")
# ================================================================================================================================ #

# ================================================================ DEVA-MAANA ================================================== #
print("# ================================================================ DEVA-MAANA ================================================== #")
# Calculate the M/R ratio for Deva-loka and it's STAR:
# Time Relation between Deva and Manushya 1 sec of Deva is 360 seconds for humans.
delta_t_deva = 1 # in secs (This is similar to delta_t_prime)
delta_t = 360 # in secs. This is including the effect of Sun's G-Field on Earth.
T = 31104000 # in secs (acc to Deva-Maana). 360 days of Deva is Time period of the planet of Deva.

# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_deva, delta_t)
print(f" Mass / Radius of Deva-loka-STAR System is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")
# Orbital Distance assuming a circular orbit is calculated as:
orbital_dist_deva = math.sqrt((G * T * T * mass_per_radius) / (4 * math.pi * math.pi))
print(f" Orbital Radius of Manu-loka is = {orbital_dist_deva:.6f} = {orbital_dist_deva:.2e} m")

# Calculating the mass of the STAR that Satyaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_devaloka = mass_per_radius * orbital_dist_deva
print(f" Mass of the STAR that Devaloka revolves around in One_AU (As Deva's One Year is 360 days) is  = {mass_of_star__of_devaloka:.12f} = {mass_of_star__of_devaloka:.2e} kg")

# Calculating Schwarzchild Radius of the star
schwarzchild_rad_of_devaloka = (2 * G * mass_of_star__of_devaloka) / (c**2)
print(f" Schwarzchild Radius of the star is = {schwarzchild_rad_of_devaloka:.6f} = {schwarzchild_rad_of_devaloka:.2e} meters...")

# Check if Schwarzchild Radius of the star = Orbital Radius of Devaloka.
if(orbital_dist_deva == schwarzchild_rad_of_devaloka):
    print("Schwarzchild Radius of the Deva-star = Orbital Radius of Devaloka")
else:
    schwarzchild_orbital_dist_diff_deva = orbital_dist_deva - schwarzchild_rad_of_devaloka
    if(schwarzchild_orbital_dist_diff_deva > 0):
        print(f" Orbital Radius of Devaloka > Schwarzchild Radius of the Deva-star by {schwarzchild_orbital_dist_diff_deva:.6f} m")
    else:
        print(f" Orbital Radius of Devaloka < Schwarzchild Radius of the Deva-star by {schwarzchild_orbital_dist_diff_deva:.6f} m")
# ================================================================================================================================ #

# ================================================================ PITRU-MAANA ================================================== #
print("# ================================================================ PITRU-MAANA ================================================== #")
# Calculate the M/R ratio for Pitru-loka and it's STAR:
# Time Relation between Pitru and Manushya 1 sec of Pitru is 30 seconds for humans.
delta_t_pitru = 1 # in secs (This is similar to delta_t_prime)
delta_t = 30 # in secs. This is including the effect of Sun's G-Field on Earth.
T = 31104000 # in secs (acc to Pitru-Maana). 360 days of Pitru is Time period of the planet of Pitru.

# M / R Ratio:
mass_per_radius = Mass_Per_Radius_GTR(G, c, delta_t_pitru, delta_t)
print(f" Mass / Radius of Pitru-loka-STAR System is = {mass_per_radius:.6f} = {mass_per_radius:.2e} Kg/m")
# Orbital Distance assuming a circular orbit is calculated as:
orbital_dist_pitru = math.sqrt((G * T * T * mass_per_radius) / (4 * math.pi * math.pi))
print(f" Orbital Radius of Manu-loka is = {orbital_dist_pitru:.6f} = {orbital_dist_pitru:.2e} m")

# Calculating the mass of the STAR that Devaloka revolves using the parameter of its revolution period as 1 year.
mass_of_star__of_pitruloka = mass_per_radius * orbital_dist_pitru
print(f" Mass of the STAR that Pitruloka revolves around in One_AU (As Pitru's One Year is 360 days) is  = {mass_of_star__of_pitruloka:.12f} = {mass_of_star__of_pitruloka:.2e} kg")

# Calculating Schwarzchild Radius of the star
schwarzchild_rad_of_pitruloka = (2 * G * mass_of_star__of_pitruloka) / (c**2)
print(f" Schwarzchild Radius of the star is = {schwarzchild_rad_of_pitruloka:.6f} = {schwarzchild_rad_of_pitruloka:.2e} meters...")

# Check if Schwarzchild Radius of the star = Orbital Radius of Satyaloka.
if(orbital_dist_pitru == schwarzchild_rad_of_pitruloka):
    print("Schwarzchild Radius of the Pitru-star = Orbital Radius of Pitruloka")
else:
    schwarzchild_orbital_dist_diff_pitru = orbital_dist_pitru - schwarzchild_rad_of_pitruloka
    if(schwarzchild_orbital_dist_diff_pitru > 0):
        print(f" Orbital Radius of Pitruloka > Schwarzchild Radius of the Pitru-star by {schwarzchild_orbital_dist_diff_pitru:.6f} m")
    else:
        print(f" Orbital Radius of Pitruloka < Schwarzchild Radius of the Pitru-star by {schwarzchild_orbital_dist_diff_pitru:.6f} m")
# ================================================================================================================================ #
