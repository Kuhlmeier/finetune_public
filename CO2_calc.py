#! /usr/bin/env python 

from pylab import * 

# https://www.ovoenergy.com/guides/energy-guides/how-much-heating-energy-do-you-use.html
kwh_m2_dk = 212. # kwh / m2

# https://ens.dk/en/our-services/statistics-data-key-figures-and-energy-maps/key-figures
co2_kwh = 364. # g/kWh
def office_heating(n_empl, associated_sqm_per_employee):
    total_energy_use = n_empl * associated_sqm_per_employee * kwh_m2_dk
    return total_energy_use * co2_kwh

# https://en.wikipedia.org/wiki/Environmental_impact_of_aviation
def air_travel(km_long, km_medium, km_short):
    return km_short*257.+km_medium*177.+km_long*113. 

# drive diesel cars that have manufacturing CO2 emission of about 120g/km, we assume 200 as rough estimate
def car_travel(approx_km):
    return 200*approx_km

#http://www.greeneatz.com/wp-content/uploads/2013/01/foods-carbon-footprint-7.gif
# we assume the fuel (food) needed to power one of us is about proportional to the hours spent... (nonconservative) 
# we also assume we work every day of the year (conservative)
def food(n_empl, hours_per_day):
    return 2.5e6*n_empl * hours_per_day/24.

n_empl = 4*1. + 3.*0.25 # 4 full time, 3 part time 

co2_office_g = office_heating(n_empl, associated_sqm_per_employee = 10.)
co2_airtravel = air_travel(2*9000*2.,2*500*2.,0)
co2_cartravel =  car_travel(10000+10000+5000+4000) # rough estimates 
co2_food = food(n_empl, hours_per_day = 8)

co2 = [ co2_office_g, co2_airtravel, co2_cartravel, co2_food]
kg_co2 = sum(co2) * 1e-3

# cloud computing on Google facilities, already carbon neutral https://cloud.google.com/environment/
# all other computing on workstations/laptops in the office, i.e. approx covered by office heating
print 'g CO2, office %.0f, air travel %.0f, car travel %.0f, food %.0f '%tuple(co2)
print 'kg CO2 used total',kg_co2

pie(co2,labels=['office heating', 'air travel', 'car travel', 'food'])
title('finetune CO2 emissions 2018, total %.0fkg'%kg_co2)
savefig('pieco2.jpg',bbox_inches='tight')




