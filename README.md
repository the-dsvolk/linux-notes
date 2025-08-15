# Linux Notes and Scripts

A comprehensive collection of Linux system administration notes and practical scripts for learning, reference, and system management.

## Project Overview

This repository is divided into two main sections:

1. **📚 Notes**: Detailed technical documentation covering Linux system internals
2. **🔧 Scripts**: Practical Python and Bash scripts for system monitoring and problem-solving

## 📚 Notes Section

Comprehensive technical documentation covering essential Linux concepts, from basic process management to advanced system internals.

### Table of Contents

| Document | Description | Key Topics |
|----------|-------------|------------|
| **[bash-process-management.md](notes/bash-process-management.md)** | Complete flow analysis of bash command execution | `fork()`, `execve()`, system calls, memory operations |
| **[process-vs-thread.md](notes/process-vs-thread.md)** | In-depth comparison of processes and threads | Memory architecture, IPC, synchronization, performance |
| **[memory.md](notes/memory.md)** | Linux memory management deep dive | Virtual memory, TLB, huge pages, `vmstat` analysis |
| **[signals.md](notes/signals.md)** | Comprehensive signal handling guide | SIGTERM, SIGKILL, SIGCHLD, signal handlers, masking |
| **[boot.md](notes/boot.md)** | Linux boot process from hardware to userspace | BIOS/UEFI, GRUB, kernel initialization, systemd |



## 🔧 Scripts Section

Practical scripts demonstrating real-world system administration and programming concepts.

### Table of Contents

| Script | Language | Purpose | Key Features |
|--------|----------|---------|--------------|
| **[dinosaur.py](scripts/dinosaur.py)** | Python | Full-featured CSV data processing | Object-oriented design, error handling, flexible parsing |
| **[dinosaur_interview.py](scripts/dinosaur_interview.py)** | Python | Interview-optimized CSV solution | Concise algorithm, clear structure, minimal dependencies |
| **[monitor_stream.py](scripts/monitor_stream.py)** | Python | Stream monitoring with alerting | Real-time processing, threshold detection, logging |
| **[monitor_simple.py](scripts/monitor_simple.py)** | Python | Minimal stream monitor | Bare-bones implementation, easy to understand |
| **[count_words.py](scripts/count_words.py)** | Python | K most frequent words with min-heap | File I/O, heap algorithms, frequency analysis |

---

**Note**: This repository serves as both educational material and practical reference for Linux system administration and development. All scripts are designed to be simple, readable, and educational rather than production-ready without proper testing and security considerations.
