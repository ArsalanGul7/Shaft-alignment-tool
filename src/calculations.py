"""
calculations.py
----------------
Engineering calculation engine
for shaft alignment.
"""
from constants import (
    LOW_SPEED_MAX_RPM,
    MEDIUM_SPEED_MAX_RPM,
    LOW_SPEED_TOLERANCE,
    MEDIUM_SPEED_TOLERANCE,
    HIGH_SPEED_TOLERANCE)
def calculate_alignment(
    rpm,
    coupling_diameter,
    front_distance,
    rear_distance,
    dial_top,
    dial_bottom):
    """
    Perform shaft alignment calculations.
    Returns:
        Dictionary containing:
        - TIR
        - Angular error
        - Shims
        - Tolerance
        - Verdict
        - RPM category
    """
    # ---------------------------------
    # Calculate TIR
    # ---------------------------------
    tir_vertical = dial_top - dial_bottom
    # ---------------------------------
    # Calculate Angular Error
    # ---------------------------------
    angular_error = (
        tir_vertical / coupling_diameter)
    # ---------------------------------
    # Calculate Foot Corrections
    # ---------------------------------
    shim_front = (
        (tir_vertical / 2)
        +
        (angular_error * front_distance))
    shim_rear = (
        (tir_vertical / 2)
        +
        (angular_error * rear_distance))
    # ---------------------------------
    # Select RPM Tolerance
    # ---------------------------------
    if rpm <= LOW_SPEED_MAX_RPM:
        tolerance = LOW_SPEED_TOLERANCE
        rpm_category = (
            "LOW SPEED MACHINE")
    elif rpm <= MEDIUM_SPEED_MAX_RPM:
        tolerance = MEDIUM_SPEED_TOLERANCE
        rpm_category = (
            "MEDIUM SPEED MACHINE")
    else:
        tolerance = HIGH_SPEED_TOLERANCE
        rpm_category = (
            "HIGH SPEED MACHINE")
    # ---------------------------------
    # Alignment Decision
    # ---------------------------------
    if abs(angular_error) <= tolerance:
        verdict = (
            "PASS - Alignment within tolerance")
    else:
        verdict = (
            "FAIL - Alignment correction required")
    # ---------------------------------
    # Return Results
    # ---------------------------------
    results = {
        "tir_vertical": tir_vertical,
        "angular_error": angular_error,
        "shim_front": shim_front,
        "shim_rear": shim_rear,
        "tolerance": tolerance,
        "rpm_category": rpm_category,
        "verdict": verdict}
    return results