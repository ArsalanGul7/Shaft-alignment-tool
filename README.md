# Shaft-alignment-tool
An open-source Python application for industrial shaft alignment calculations and maintenance reporting.

## Overview
A Python-based engineering application for shaft alignment analysis using dial indicator measurements.
The software calculates:
- Vertical TIR
- Angular alignment error
- Front foot correction
- Rear foot correction
- RPM based tolerance evaluation
- PASS / FAIL alignment status
## Features
- Engineer identification
- Graphical user interface
- Input validation
- Automatic engineering calculations
- Automatic alignment report generation
- RPM based tolerance selection
## Operating Range
Supported machine speed:
400 RPM - 1500 RPM


## RPM Tolerance Classification

|    RPM Range  |  Category  | Tolerance  |
|---------------|------------|------------|
|400 - 900 RPM  |Low Speed   |0.15 mm/inch|
|901 - 1200 RPM |Medium Speed|0.10 mm/inch|
|1201 - 1500 RPM|High Speed  |0.07 mm/inch|


## Project Structure
Shaft-alignment-tool

├── src
│ ├── main.py
│ ├── gui.py
│ ├── calculations.py
│ ├── validation.py
│ ├── report.py
│ └── constants.py
│
├── reports
├── docs
├── screenshots
└── sample_data


## Technology

- Python 3
- Tkinter GUI


## Running the Application

Run:
python src/main.py

## Generated Reports
Alignment reports are automatically created in:
reports/
## Author
Syed Arsalan Gul
## License
MIT License
