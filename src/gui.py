"""
gui.py
----------------
Tkinter graphical interface
for Shaft Alignment Tool.
"""
import tkinter as tk
from tkinter import messagebox
from constants import (
    APP_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR,
    HEADER_COLOR,
    BUTTON_COLOR,
    BUTTON_ACTIVE_COLOR,
    REPORT_FILENAME)
from validation import validate_inputs
from calculations import calculate_alignment
from report import generate_report
class ShaftAlignmentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(
            APP_TITLE)
        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(
            bg=BACKGROUND_COLOR)
        self.create_header()
        self.create_input_area()
        self.create_button()
    # ---------------------------------
    # Header
    # ---------------------------------
    def create_header(self):
        header = tk.Label(
            self.root,
            text=APP_TITLE,
            font=(
                "Arial",
                12,
                "bold"),
            bg=HEADER_COLOR,
            pady=12)
        header.pack(
            fill=tk.X)
    # ---------------------------------
    # Input Section
    # ---------------------------------
    def create_input_area(self):
        frame = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOR,
            padx=25,
            pady=15)
        frame.pack(
            fill=tk.BOTH,
            expand=True)
        self.engineer_entry = self.create_field(
            frame,
            "Engineer Name:")
        self.rpm_entry = self.create_field(
            frame,
            "Machine RPM:")
        self.diameter_entry = self.create_field(
            frame,
            "Coupling Diameter (mm):")
        self.front_entry = self.create_field(
            frame,
            "Front Foot Distance (mm):")
        self.rear_entry = self.create_field(
            frame,
            "Rear Foot Distance (mm):")
        self.top_entry = self.create_field(
            frame,
            "Dial Top Reading:")
        self.bottom_entry = self.create_field(
            frame,
            "Dial Bottom Reading:")
        self.result_label = tk.Label(
            frame,
            text="",
            bg=BACKGROUND_COLOR,
            font=(
                "Arial",
                10,
                "bold"),
            wraplength=400)
        self.result_label.pack(
            pady=15)
    # ---------------------------------
    # Create Entry Row
    # ---------------------------------
    def create_field(
        self,
        frame,
        label_text):
        row = tk.Frame(
            frame,
            bg=BACKGROUND_COLOR,
            pady=6)
        row.pack(
            fill=tk.X)
        label = tk.Label(
            row,
            text=label_text,
            bg=BACKGROUND_COLOR,
            width=25,
            anchor="w")
        label.pack(
            side=tk.LEFT)
        entry = tk.Entry(
            row,
            width=15)
        entry.pack(
            side=tk.RIGHT)
        return entry
    # ---------------------------------
    # Button
    # ---------------------------------
    def create_button(self):
        button = tk.Button(
            self.root,
            text="CALCULATE ALIGNMENT",
            font=(
                "Arial",
                10,
                "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            activebackground=BUTTON_ACTIVE_COLOR,
            pady=10,
            command=self.process_alignment)
        button.pack(
            fill=tk.X,
            padx=25,
            pady=20)
    # ---------------------------------
    # Processing
    # ---------------------------------
    def process_alignment(self):
        engineer = self.engineer_entry.get()
        rpm = self.rpm_entry.get()
        diameter = self.diameter_entry.get()
        front = self.front_entry.get()
        rear = self.rear_entry.get()
        top = self.top_entry.get()
        bottom = self.bottom_entry.get()
        valid, message = validate_inputs(
            engineer,
            rpm,
            diameter,
            front,
            rear,
            top,
            bottom)
        if not valid:
            messagebox.showerror(
                "Input Error",
                message)
            return
        rpm = int(rpm)
        diameter = float(diameter)
        front = float(front)
        rear = float(rear)
        top = float(top)
        bottom = float(bottom)
        results = calculate_alignment(
            rpm,
            diameter,
            front,
            rear,
            top,
            bottom)
        report_file = generate_report(
            engineer,
            rpm,
            diameter,
            results)
        output = (
            f"{results['verdict']}\n\n"
            f"RPM Category:\n"
            f"{results['rpm_category']}\n\n"
            f"Front Shim:\n"
            f"{results['shim_front']:.3f} mm\n\n"
            f"Rear Shim:\n"
            f"{results['shim_rear']:.3f} mm\n\n"
            f"Report Saved:\n"
            f"{report_file}")
        self.result_label.config(
            text=output)
        messagebox.showinfo(
            "Alignment Complete",
            "Alignment report generated successfully.")