import tkinter as tk
from tkinter import ttk, messagebox
import threading
import psutil
import time
import random


class AdaptiveResourceAllocationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive Resource Allocation System")
        self.root.geometry("600x400")

        # Resource thresholds
        self.cpu_threshold = tk.DoubleVar(value=80.0)
        self.memory_threshold = tk.DoubleVar(value=80.0)

        # GUI Layout
        self.create_widgets()

        # Stop flag for monitoring
        self.monitoring = False

    def create_widgets(self):
        # CPU Threshold
        tk.Label(self.root, text="CPU Threshold (%)").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.cpu_threshold_entry = ttk.Entry(self.root, textvariable=self.cpu_threshold, width=10)
        self.cpu_threshold_entry.grid(row=0, column=1, padx=10, pady=10)

        # Memory Threshold
        tk.Label(self.root, text="Memory Threshold (%)").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.memory_threshold_entry = ttk.Entry(self.root, textvariable=self.memory_threshold, width=10)
        self.memory_threshold_entry.grid(row=1, column=1, padx=10, pady=10)

        # Start/Stop Buttons
        self.start_button = ttk.Button(self.root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop Monitoring", command=self.stop_monitoring, state="disabled")
        self.stop_button.grid(row=2, column=1, padx=10, pady=10)

        # Resource Display
        self.status_label = tk.Label(self.root, text="System Status", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=2, pady=20)

        self.cpu_label = tk.Label(self.root, text="CPU Usage: 0%", font=("Arial", 12))
        self.cpu_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.memory_label = tk.Label(self.root, text="Memory Usage: 0%", font=("Arial", 12))
        self.memory_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Listbox for Program Simulation
        tk.Label(self.root, text="Simulated Programs").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.program_listbox = tk.Listbox(self.root, width=50, height=10)
        self.program_listbox.grid(row=6, column=1, padx=10, pady=10)

    def start_monitoring(self):
        """Start Resource Monitoring"""
        self.monitoring = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        # Start monitoring in a separate thread
        self.monitor_thread = threading.Thread(target=self.monitor_resources, daemon=True)
        self.monitor_thread.start()

        # Simulate programs in a separate thread
        self.simulation_thread = threading.Thread(target=self.simulate_programs, daemon=True)
        self.simulation_thread.start()

    def stop_monitoring(self):
        """Stop Resource Monitoring"""
        self.monitoring = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def monitor_resources(self):
        """Monitor CPU and Memory Resources"""
        while self.monitoring:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            # Update labels
            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

            # Check thresholds
            if cpu_usage > self.cpu_threshold.get():
                self.status_label.config(text="High CPU Usage Detected!", fg="red")
                self.throttle_low_priority_programs()
            elif memory_usage > self.memory_threshold.get():
                self.status_label.config(text="High Memory Usage Detected!", fg="red")
                self.reduce_memory_usage()
            else:
                self.status_label.config(text="System Status: Normal", fg="green")

            time.sleep(1)

    def simulate_programs(self):
        """Simulate multiple programs with resource usage"""
        while self.monitoring:
            program_name = f"Program_{random.randint(1, 100)}"
            cpu_usage = random.uniform(5, 20)
            memory_usage = random.uniform(50, 200)

            self.program_listbox.insert(tk.END, f"{program_name} - CPU: {cpu_usage:.1f}%, Memory: {memory_usage:.1f}MB")
            self.program_listbox.see(tk.END)

            # Limit the listbox size
            if self.program_listbox.size() > 20:
                self.program_listbox.delete(0)

            time.sleep(3)

    def throttle_low_priority_programs(self):
        """Throttle simulated low-priority programs (example logic)"""
        if self.program_listbox.size() > 0:
            low_priority_program = self.program_listbox.get(0)
            self.program_listbox.delete(0)
            self.program_listbox.insert(tk.END, f"Throttled: {low_priority_program}")

    def reduce_memory_usage(self):
        """Reduce memory usage by removing simulated programs"""
        if self.program_listbox.size() > 0:
            removed_program = self.program_listbox.get(0)
            self.program_listbox.delete(0)
            self.program_listbox.insert(tk.END, f"Memory Reduced: {removed_program}")


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdaptiveResourceAllocationGUI(root)
    root.mainloop()