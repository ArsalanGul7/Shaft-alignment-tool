"""
constants.py
----------------
Central configuration settings
for the Shaft Alignment Tool.
"""
# -----------------------------
# Application Information
# -----------------------------
APP_TITLE = "Shaft Alignment Tool"
APP_VERSION = "1.0.0"
# -----------------------------
# Window Settings
# -----------------------------
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 620
# -----------------------------
# Report Settings
# -----------------------------
REPORT_FOLDER = "reports"
REPORT_FILENAME = "Shaft_Alignment_Report.txt"
# -----------------------------
# Machine RPM Limits
# -----------------------------
MIN_RPM = 400
MAX_RPM = 1500
# -----------------------------
# RPM Categories
# -----------------------------
LOW_SPEED_MAX_RPM = 900
MEDIUM_SPEED_MAX_RPM = 1200
# -----------------------------
# Alignment Tolerances
# Unit: mm/inch
# -----------------------------
LOW_SPEED_TOLERANCE = 0.15
MEDIUM_SPEED_TOLERANCE = 0.10
HIGH_SPEED_TOLERANCE = 0.07
# -----------------------------
# GUI Appearance
# -----------------------------
BACKGROUND_COLOR = "#f4f4f6"
HEADER_COLOR = "#e2e8f0"
BUTTON_COLOR = "#2b6cb0"
BUTTON_ACTIVE_COLOR = "#2c5282"