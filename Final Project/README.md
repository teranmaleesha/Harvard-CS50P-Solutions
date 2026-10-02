# Radioactive Decay & Half-Life Calculator

#### Video Demo: <https://youtu.be/hnzHA3R-pnQ?si=RXku2yEUsypoLa9U>

#### Description:
The **Radioactive Decay & Half-Life Calculator** is a Python-based command-line interface (CLI) application created as the final project for Harvard's CS50P (CS50's Introduction to Programming with Python) course. The project combines core concepts of Nuclear Physics with Python programming principles to model the process of radioactive decay over time.

##### Overview and Background
Radioactive decay is the process by which an unstable atomic nucleus loses energy by radiation. A material containing unstable nuclei is considered radioactive. The decay of a given nucleus is entirely random, but for a large group of atoms, the decay rate can be precisely calculated using exponential decay laws. This project uses fundamental nuclear physics equations to calculate the remaining number of radioactive particles after a given period, based on the initial quantity and the isotope's specific half-life.

##### Features and Logic
The project consists of three main modular functions apart from the `main()` controller, adhering to CS50P design standards:

1. `get_half_life(isotope)`:
   - Takes the common name of a radioactive isotope as input (e.g., Carbon-14, Uranium-238, Cobalt-60, Iodine-131).
   - Searches an internal database (Python dictionary) and returns its half-life in years.
   - Raises a `ValueError` if the requested isotope is not found in the database.

2. `calculate_decay_constant(half_life)`:
   - Calculates the decay constant using the formula: lambda = ln(2) / T_1/2.
   - Ensures that the provided half-life is greater than zero to avoid division by zero errors or non-physical negative half-lives.

3. `calculate_remaining_particles(n0, decay_constant, time)`:
   - Computes the remaining number of particles N(t) after time t using the decay formula: N(t) = N0 * e^(-lambda * t).
   - Validates that initial particle counts and elapsed times are non-negative.

##### Project Structure
- `project.py`: Contains the main application code and business logic functions.
- `test_project.py`: Contains automated unit tests written with `pytest` to verify the accuracy and error-handling capabilities of all three primary functions.
- `README.md`: Provides comprehensive documentation for the project.

##### How to Run
To run the application, execute:
```bash
python project.py
