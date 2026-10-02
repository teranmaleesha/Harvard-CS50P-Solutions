import pytest
from project import get_half_life, calculate_decay_constant, calculate_remaining_particles
def test_get_half_life():
    assert get_half_life("carbon-14") == 5730
    assert get_half_life("cobalt-60") == 5.27
    with pytest.raises(ValueError):
        get_half_life("unknown-isotope")
def test_calculate_decay_constant():
    assert round(calculate_decay_constant(5730), 8) == 0.00012097
    with pytest.raises(ValueError):
        calculate_decay_constant(0)
def test_calculate_remaining_particles():
    # half-life 5730 (decay_constant ~0.00012097), years 5730 නම් N0 1000න් භාගයක් (500) ඉතිරි විය යුතුය
    decay_constant = calculate_decay_constant(5730)
    assert round(calculate_remaining_particles(1000, decay_constant, 5730), 2) == 500.0
    with pytest.raises(ValueError):
        calculate_remaining_particles(-100, decay_constant, 10)
