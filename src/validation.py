"""
validation.py
----------------
Input validation module.

Checks all shaft alignment
inputs before calculations.
"""
from constants import MIN_RPM, MAX_RPM
def validate_inputs(
    engineer_name,
    rpm,
    coupling_diameter,
    front_distance,
    rear_distance,
    dial_top,
    dial_bottom):
    """
    Validate all engineering inputs.
    Returns:
        (True, "")
        or
        (False, error message)
    """
    # Check engineer name
    if engineer_name.strip() == "":
        return False, "Engineer name is required."
    # Convert numerical inputs
    try:
        rpm = int(rpm)
        coupling_diameter = float(coupling_diameter)
        front_distance = float(front_distance)
        rear_distance = float(rear_distance)
        dial_top = float(dial_top)
        dial_bottom = float(dial_bottom)
    except ValueError:
        return False, "All measurement fields must contain valid numbers."
    # RPM range validation
    if rpm < MIN_RPM or rpm > MAX_RPM:
        return (
            False,
            f"RPM must be between {MIN_RPM} and {MAX_RPM}.")
    # Coupling check
    if coupling_diameter <= 0:
        return False, "Coupling diameter must be greater than zero."
    # Distance checks
    if front_distance < 0:
        return False, "Front foot distance cannot be negative."
    if rear_distance < 0:
        return False, "Rear foot distance cannot be negative."
    # Dial indicator checks
    if dial_top < -10 or dial_top > 10:
        return False, "Top dial reading is outside expected range."
    if dial_bottom < -10 or dial_bottom > 10:
        return False, "Bottom dial reading is outside expected range."
    return True, ""