"""
report.py
----------------
Engineering report generation module.

Creates professional shaft alignment
inspection reports.
"""
import os
from datetime import datetime
from constants import REPORT_FOLDER
def generate_report(
    engineer_name,
    rpm,
    coupling_diameter,
    results):
    """
    Generate shaft alignment report.
    Parameters:
        engineer_name : str
        rpm            : int
        coupling_diameter : float
        results        : dict from calculations.py
    Returns:
        Report file path
    """
    # ---------------------------------
    # Create reports folder if missing
    # ---------------------------------
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)
    # ---------------------------------
    # Report filename
    # ---------------------------------
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S")
    filename = (
        f"Shaft_Alignment_Report_{timestamp}.txt")
    filepath = os.path.join(
        REPORT_FOLDER,
        filename)
    # ---------------------------------
    # Write Report
    # ---------------------------------
    with open(filepath, "w") as report:
        report.write(
            "=" * 65 + "\n")
        report.write(
            "SHAFT ALIGNMENT ENGINEERING REPORT\n")
        report.write(
            "=" * 65 + "\n\n")
        report.write(
            "GENERAL INFORMATION\n")
        report.write(
            "-" * 65 + "\n")
        report.write(
            f"Date / Time       : "
            f"{datetime.now()}\n")
        report.write(
            f"Engineer Name     : "
            f"{engineer_name}\n\n")
        report.write(
            "MACHINE INFORMATION\n")
        report.write(
            "-" * 65 + "\n")
        report.write(
            f"Operating RPM     : "
            f"{rpm}\n")
        report.write(
            f"Coupling Diameter : "
            f"{coupling_diameter} mm\n\n")
        report.write(
            "ALIGNMENT RESULTS\n")
        report.write(
            "-" * 65 + "\n")
        report.write(
            f"RPM Category      : "
            f"{results['rpm_category']}\n")
        report.write(
            f"Allowed Tolerance : "
            f"{results['tolerance']:.3f} mm/inch\n\n")
        report.write(
            f"TIR Vertical     : "
            f"{results['tir_vertical']:.4f} mm\n")
        report.write(
            f"Angular Error    : "
            f"{results['angular_error']:.4f}\n")
        report.write(
            f"Front Shim       : "
            f"{results['shim_front']:.3f} mm\n")
        report.write(
            f"Rear Shim        : "
            f"{results['shim_rear']:.3f} mm\n\n")
        report.write(
            "FINAL RESULT\n")
        report.write(
            "-" * 65 + "\n")
        report.write(
            f"{results['verdict']}\n")
        report.write(
            "\n")
        report.write(
            "=" * 65 + "\n")
    return filepath