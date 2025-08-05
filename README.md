
This is not meant to be a functional script, but rather a project to practice OOP concepts, crud operations using SQLITE and basics of FASTAPI.


### Features

Add, remove, and display cars.
Modify engine aspiration (for combustion cars only).
Automatic horsepower calculation based on engine capacity + aspiration type (for combustion) or kW (for electric).


### Structure

Main Class GarageManager to append/remove/show cars 

Parent Class Car with commun attributes between diferent types of cars

Two children Classes:
  - ElectricCar
  - CombustionCar

### Car Behavior

The only method that changes car behavior is modify engine aspiration
