#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:43:53 2024

Arbeidskrav 1 Compare car types regards to yearly cost

@author: gunnhelenedrogset
"""


def yearly_car_cost(yearly_km, insurance_cost, yearly_traffic_insurance, cost_pr_km, toll_pr_km):
    
    yearly_car_cost = insurance_cost + yearly_traffic_insurance + yearly_km*cost_pr_km + yearly_km*toll_pr_km
    return yearly_car_cost




yearly_km = float(input("Hvor mange km kjører du årlig? "))
traffic_insurance = 8.38                            # kr/day
yearly_traffic_insurance = traffic_insurance * 365  # kr/day * days a year, common for both car types
insurance_gasoline_car = 7500                       # kr yearly
insurance_electric_car = 5000                       # kr yearly
toll_electric_pr_km = 0.1                           # kr/km
toll_gasoline_pr_km =0.3                            # kr/km
kWh_pr_km = 0.2                                     # kWh/km
cost_pr_kWh = 2.00                                  # kr/kWh
electricity_cost_pr_km = kWh_pr_km*cost_pr_kWh      # kr/km
gasoline_cost_pr_km = 1.0                           # kr/km


gasoline_car_cost = yearly_car_cost(yearly_km, insurance_gasoline_car, yearly_traffic_insurance, gasoline_cost_pr_km, toll_gasoline_pr_km)
electric_car_cost = yearly_car_cost(yearly_km, insurance_electric_car, yearly_traffic_insurance, electricity_cost_pr_km, toll_electric_pr_km)

print(f"Kostnaden for en bensinbil er {gasoline_car_cost:.2f} kr årlig når du kjører {yearly_km} km") 
print(f"Kostnaden for en elbil er {electric_car_cost:.2f} kr årlig når du kjører {yearly_km} km") 

if gasoline_car_cost < electric_car_cost: 
    print("Det lønner seg å kjøpe bensinbil!")
elif gasoline_car_cost == electric_car_cost: 
    print("Elbil og bensinbil koster like mye")
else:  
    print("Det lønner seg å kjøpe elbil!")
    