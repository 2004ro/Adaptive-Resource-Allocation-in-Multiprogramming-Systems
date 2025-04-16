# Adaptive-Resource-Allocation-in-Multiprogramming-Systems
A System that dynamically adjusts resource allocation among  multiple programs to optimize CPU and memory utilization. The solution should monitor  system performance and reallocate resources in real-time to prevent bottlenecks.

# Project Overview
A dynamic resource allocation framework operates within multiprogramming environments where it runs through Python programming code. Real-time CPU and memory usage tracking by the system initiates resource distribution between programs after utility-defined thresholds are breached. The Tkinter GUI provides user interface visibility for the system along with performance improvement demonstrations that overcome system blocking problems.


# Problem Statement
A multiprogramming system operates multiple concurrently running programs that both share computer resources such as CPU time and memory capacity. Without dynamic management these computer systems encounter insufficient performance and functional decline and system crashes. A real-time adaptive resource monitoring system represents the primary solution explained within this project.


# Objectives
The system provides continuous observation of CPU performance and memory consumption levels.
The system should execute simulations which use programs that need different resources.
The system should implement real-time resource allocation and reduction strategies when monitoring threshold levels are reached.
The system presents textual and visual depictions which show program execution and system operational status.
The system prevents performance reductions which occur because of excessive system resource utilization.

# Methodology

# System Architecture
**Frontend:** Tkinter GUI
  **Backend:** The system implements a Backend section based on Python code alongside psutil and threading applications.
**Modules:**
  - Resource monitor thread (real-time stats)
  The second thread simulates programs through randomly generated usage.
  The system contains an adaptive control mechanism which performs resource reduction or throttling operations.


# Algorithms
**Monitoring:** Periodically fetches CPU/memory stats and compares to thresholds.
- *Adaptive Logic: 
  - If CPU > threshold -> Throttle (Slow down or remove background/simulated programs that are less important to reduce CPU usage)low-priority programs.
  The system will either eliminate completely or cut down simulated software processes when memory usage exceeds the set threshold value.

#  Technologies Used
| Component          | Tool/Library        |
|-------------------|---------------------|
| Programming Lang. | Python              |
| GUI               | Tkinter             |
| Monitoring        | psutil              |
The implementation of threading serves as the concurrent execution system.
| Visualization     |


#  Case Studies
## Case Study 1
- **CPU Threshold:** 70%
- **Memory Threshold:** 80%
- **Simulated Programs:** 10
The system adapted when memory consumption exceeded 75% but the CPU remained stable. Memory usage stabilized without overloading.

## Case Study 2
- **CPU Threshold:** 60%
- **Memory Threshold:** 75%
- **Simulated Programs:** 8
  
The system adapted when memory consumption exceeded 75% but the CPU remained stable. Memory usage stabilized without overloading.



##  Sample Output

```text
CPU Usage: 80%
Memory Usage: 80%
Status: System Status: Normal

Program_39 - CPU: 10.9%, Memory: 146.2MB

Memory Reduced: Program_39 - CPU: 6.4%, Memory: 77.0MB
