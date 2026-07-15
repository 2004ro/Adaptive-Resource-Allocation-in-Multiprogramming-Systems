# 🖥️ Adaptive Resource Allocation in Multiprogramming Systems

A Python-based simulation system that monitors CPU and memory utilization in real time and demonstrates adaptive resource management strategies in a multiprogramming environment.

The application uses a Tkinter-based graphical interface to simulate program execution and apply threshold-based actions such as throttling low-priority tasks and reducing memory usage when system resources exceed predefined limits.

---

## 📌 Project Overview

In a multiprogramming environment, multiple programs compete for limited system resources such as CPU and memory. Excessive resource consumption can lead to performance degradation and reduced system responsiveness.

This project simulates an adaptive resource allocation mechanism that continuously monitors system resource usage and performs corrective actions when utilization exceeds user-defined thresholds.

---

## 🎯 Objectives

- Monitor CPU utilization in real time.
- Monitor memory utilization in real time.
- Simulate multiple programs with varying resource requirements.
- Apply threshold-based resource management strategies.
- Demonstrate adaptive resource allocation concepts.
- Provide a graphical interface for monitoring system performance.

---

## ✨ Features

### Real-Time Resource Monitoring
- Live CPU usage monitoring using psutil.
- Live memory usage monitoring.
- Dynamic status updates based on system conditions.

### User-Defined Thresholds
- Custom CPU utilization threshold.
- Custom memory utilization threshold.
- Interactive threshold configuration through GUI.

### Program Simulation
- Simulates multiple running programs.
- Generates varying CPU and memory workloads.
- Displays active program information.

### Adaptive Resource Management
- Throttles low-priority simulated programs when CPU usage exceeds the threshold.
- Reduces memory load by removing simulated programs when memory usage exceeds the threshold.
- Demonstrates threshold-based resource management strategies.

### Graphical User Interface
- Built using Tkinter.
- Interactive monitoring dashboard.
- Real-time status display.

---

## 🛠️ Technologies Used

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| GUI Framework | Tkinter |
| System Monitoring | psutil |
| Multithreading | threading |
| Simulation | random |
| Time Management | time |

---

## 🏗️ System Architecture

### Resource Monitoring Module
Continuously tracks CPU and memory utilization using the psutil library.

### Program Simulation Module
Generates simulated programs with random CPU and memory consumption patterns.

### Adaptive Control Module
Applies threshold-based actions to reduce system load when resource utilization exceeds predefined limits.

### User Interface Module
Provides real-time visualization of system status and simulated program activity.

---

## ⚙️ Working Principle

1. User specifies CPU and memory thresholds.
2. Resource monitoring begins.
3. Simulated programs are generated continuously.
4. System usage is monitored in real time.
5. When CPU usage exceeds the threshold:
   - Low-priority simulated programs are throttled.
6. When memory usage exceeds the threshold:
   - Simulated programs are removed to reduce memory load.
7. Updated system status is displayed through the GUI.

---

## 📂 Project Structure

```text
Adaptive-Resource-Allocation/
│
├── main.py
├── background1.jpg
├── background2.jpg
├── background3.jpg
└── README.md
```

---

## 🖥️ Sample Output

```text
CPU Usage: 82%
Memory Usage: 76%

Status: High CPU Usage Detected!

Program_42 - CPU: 15.6%, Memory: 125.4MB

Throttled: Program_42
```

---

## 📚 Concepts Demonstrated

- Multiprogramming
- Resource Allocation
- CPU Scheduling Concepts
- Memory Management Concepts
- System Monitoring
- Multithreading
- GUI Development
- Operating System Fundamentals

---

## 🚀 Future Enhancements

- Real process monitoring and management.
- Resource usage visualization using charts and graphs.
- Process prioritization algorithms.
- Advanced scheduling techniques.
- Historical resource usage analytics.
- Database integration for logging and reporting.
- Web-based monitoring dashboard.

---

## 🎓 Learning Outcomes

- Operating System Concepts
- Python Application Development
- Tkinter GUI Programming
- Multithreading in Python
- System Resource Monitoring
- Adaptive Control Strategies
- Software Design and Simulation

