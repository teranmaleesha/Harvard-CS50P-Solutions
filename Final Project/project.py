import math
def main():
    print("--- Radioactive Decay Calculator ---")
    isotope = input("Enter isotope (e.g., carbon-14, uranium-238, cobalt-60): ").strip().lower()
    try:
        half_life = get_half_life(isotope)
        print(f"Half-life of {isotope.capitalize()}: {half_life} years")
        n0 = float(input("Enter initial number of particles (N0): "))
        time = float(input("Enter elapsed time (in years): "))
        decay_constant = calculate_decay_constant(half_life)
        remaining = calculate_remaining_particles(n0, decay_constant, time)
        print(f"Remaining particles after {time} years: {remaining:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
def get_half_life(isotope):
    data = {
        "carbon-14": 5730,
        "uranium-238": 4468000000,
        "cobalt-60": 5.27,
        "iodine-131": 0.022,
    }
    if isotope in data:
        return data[isotope]
    else:
        raise ValueError("Isotope not found in database")
def calculate_decay_constant(half_life):
    if half_life <= 0:
        raise ValueError("Half-life must be greater than zero")
    return math.log(2) / half_life
def calculate_remaining_particles(n0, decay_constant, time):
    if n0 < 0 or time < 0:
        raise ValueError("Initial particles and time must be non-negative")
    # N(t) = N0 * e^(-lambda * t)
    return n0 * math.exp(-decay_constant * time)
if __name__ == "__main__":
    main()
