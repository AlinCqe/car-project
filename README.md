A simple Object Oriented program to practice working with classes.

This is not meant to be a functional script, but rather a project to practice OOP concepts.

## Project Structure

- `cli_project/`
The terminal-based version of the app where you interact via command-line inputs.

- `api_project/`
The FastAPI-based version exposing a web API for managing cars through HTTP requests.

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




Planned improvements include adding more methods like driving, charging the battery...
