# 🚀 Math King Calculator + To-Do List Application

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717.svg?logo=github)](https://github.com/bio-computerinteranthusasum786/math-king-calculator)
[![Last Commit](https://img.shields.io/github/last-commit/bio-computerinteranthusasum786/math-king-calculator)]

A powerful dual-purpose application combining a **scientific calculator with 250+ mathematical functions** and a **to-do list manager with local storage**.

## 📑 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Components](#-components)
- [Documentation](#-documentation)
- [Examples](#-examples)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🧮 Scientific Calculator (250+ Functions)

- **Basic Arithmetic**: add, subtract, multiply, divide, power, modulo, etc.
- **Trigonometric**: sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, etc.
- **Logarithmic & Exponential**: log, log10, log2, ln, exp, sqrt, cbrt, etc.
- **Number Theory**: factorial, fibonacci, gcd, lcm, prime checks, divisors, etc.
- **Statistical**: mean, median, mode, variance, std_dev, percentiles, etc.
- **Combinatorics**: combinations, permutations, derangements, etc.
- **Complex Numbers**: complex arithmetic, polar conversion, etc.
- **Financial Math**: compound interest, loan payments, NPV, ROI, etc.
- **Geometry**: circle, sphere, triangle, cylinder volumes, distances, etc.
- **Matrix Operations**: Basic matrix math (expansion planned)
- **Calculus**: Numerical derivatives, integrals, Taylor series, etc.
- **Utility Functions**: Rounding, clipping, lerp, range mapping, etc.

### 📝 To-Do List Application (Local Storage)

- **Task Management**: Create, read, update, delete tasks
- **Local Storage**: Auto-save to JSON (`todos.json`)
- **Priorities**: Low, Medium, High, Urgent levels
- **Due Dates**: Track deadlines with overdue detection
- **Tags**: Organize tasks by categories
- **Search & Filter**: Find tasks by title, tag, priority, or date
- **Statistics**: View completion rates and task breakdowns
- **Export/Import**: Backup and restore tasks
- **Interactive CLI**: User-friendly command interface

---

## 🚀 Quick Start

### Scientific Calculator

```bash
python calculator.py

> add 5 3
Result: 8

> sin 1.5708
Result: 1.0

> factorial 5
Result: 120

> gcd 48 18
Result: 6
```

### To-Do List

```bash
python todo_app.py

> add Buy groceries
  Description: Milk, eggs, bread
  Priority: medium
  Due date: 2026-07-05
  Tags: shopping

> list
> complete <task-id>
> stats
```

---

## 📦 Installation

### Requirements

- Python 3.7 or higher
- pip (Python package manager)

### Setup

```bash
# Clone the repository
git clone https://github.com/bio-computerinteranthusasum786/math-king-calculator.git
cd math-king-calculator

# Install dependencies (optional, for advanced features)
pip install -r requirements.txt

# Run calculator
python calculator.py

# Run to-do list
python todo_app.py
```

---

## 💻 Usage

### Using the Calculator

**Interactive Mode:**
```bash
python calculator.py
```

**As a Python Library:**
```python
from calculator import MathKingCalculator

calc = MathKingCalculator()

# Basic operations
print(calc.add(10, 5))           # 15
print(calc.multiply(4, 7))       # 28

# Trigonometry
print(calc.sin(3.14159/2))       # ~1.0
print(calc.cos(0))               # 1.0

# Number theory
print(calc.factorial(5))         # 120
print(calc.gcd(48, 18))          # 6

# Statistics
data = [1, 2, 3, 4, 5]
print(calc.mean(data))           # 3
print(calc.std_dev(data))        # ~1.414
```

### Using the To-Do List

**Interactive Mode:**
```bash
python todo_app.py
```

**Commands:**
```bash
add <title>           # Add new task
list                  # Show all tasks
list-pending          # Show incomplete tasks
complete <id>         # Mark task done
priority <level>      # Filter by priority
tag <name>            # Filter by tag
search <query>        # Search tasks
stats                 # Show statistics
export <file>        # Backup tasks
import <file>        # Restore tasks
quit                  # Exit
```

**As a Python Library:**
```python
from todo_app import TodoList

todo_list = TodoList()

# Add task
task = todo_list.add_task(
    title="Learn Python",
    description="Complete online course",
    priority="high",
    due_date="2026-08-01",
    tags=["learning", "python"]
)

# Get tasks
pending = todo_list.get_pending_tasks()
print(f"Pending: {len(pending)} tasks")

# Statistics
stats = todo_list.get_statistics()
print(f"Completion rate: {stats['completion_rate']}")

# Export
todo_list.export_to_file("backup.json")
```

---

## 📂 Components

### Core Files

| File | Purpose |
|------|----------|
| `calculator.py` | Scientific calculator with 250+ functions |
| `todo_app.py` | To-do list application with local storage |
| `todos.json` | Auto-generated storage for tasks |
| `requirements.txt` | Python dependencies (NumPy, SciPy) |

### Documentation Files

| File | Description |
|------|-------------|
| `README.md` | This file - overview and quick start |
| `FUNCTIONS.md` | Complete calculator function reference |
| `TODO_APP_GUIDE.md` | To-do list user guide and commands |
| `TODO_API_REFERENCE.md` | To-do list API documentation |
| `EXAMPLES.md` | Practical usage examples |

---

## 📚 Documentation

### Calculator Documentation
- **[FUNCTIONS.md](FUNCTIONS.md)** - Complete reference of all 250+ functions with examples
- Organized by category (Arithmetic, Trigonometry, Statistics, etc.)
- Each function includes description and usage examples

### To-Do List Documentation
- **[TODO_APP_GUIDE.md](TODO_APP_GUIDE.md)** - User-friendly guide and command reference
- **[TODO_API_REFERENCE.md](TODO_API_REFERENCE.md)** - Complete API documentation for developers
- **[EXAMPLES.md](EXAMPLES.md)** - 10+ practical examples and workflows

---

## 🎯 Examples

### Example 1: Basic Calculations

```bash
> add 100 50
150

> multiply 12 5
60

> power 2 10
1024

> sqrt 144
12.0
```

### Example 2: Mathematical Analysis

```python
from calculator import MathKingCalculator

calc = MathKingCalculator()

# Fibonacci sequence
for i in range(10):
    print(calc.fibonacci(i))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Prime check
for n in [17, 18, 19, 20, 21]:
    print(f"{n}: {calc.is_prime(n)}")

# Statistical analysis
data = [10, 20, 30, 40, 50]
print(f"Mean: {calc.mean(data)}")
print(f"Median: {calc.median(data)}")
print(f"Std Dev: {calc.std_dev(data)}")
```

### Example 3: Task Management

```bash
# Add tasks
> add "Design database"
  Priority: high
  Tags: project, database

> add "Write API endpoints"
  Priority: high
  Tags: project, backend

# View by priority
> priority high

# Check statistics
> stats

# Export for backup
> export project_tasks.json
```

See **[EXAMPLES.md](EXAMPLES.md)** for more detailed examples.

---

## 🔌 API Reference

### Calculator API

```python
from calculator import MathKingCalculator

calc = MathKingCalculator()

# Arithmetic
calc.add(5, 3)           # 8
calc.subtract(10, 3)     # 7
calc.multiply(4, 5)      # 20
calc.divide(10, 2)       # 5.0

# Trigonometry
calc.sin(3.14159/2)      # ~1.0
calc.cos(0)              # 1.0
calc.tan(3.14159/4)      # ~1.0

# Statistics
calc.mean([1, 2, 3])     # 2.0
calc.median([1, 2, 3])   # 2
calc.std_dev([1, 2, 3])  # ~0.816
```

See **[FUNCTIONS.md](FUNCTIONS.md)** for all 250+ functions.

### To-Do List API

```python
from todo_app import TodoList

todo_list = TodoList()

# CRUD
task = todo_list.add_task(title="...", priority="high")
todo_list.update_task(task_id, title="...")
todo_list.delete_task(task_id)

# Filtering
pending = todo_list.get_pending_tasks()
completed = todo_list.get_completed_tasks()
high = todo_list.get_tasks_by_priority("high")

# Utilities
todo_list.complete_task(task_id)
todo_list.export_to_file("backup.json")
stats = todo_list.get_statistics()
```

See **[TODO_API_REFERENCE.md](TODO_API_REFERENCE.md)** for complete API docs.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Areas for Contribution

- Additional mathematical functions
- Matrix operations expansion
- Web interface for to-do list
- Mobile app support
- Performance optimizations
- Bug fixes and improvements
- Documentation enhancements

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

```
MIT License

Copyright (c) 2026 bio-computerinteranthusasum786

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📊 Project Statistics

- **Total Functions**: 250+
- **Calculator Categories**: 14
- **To-Do List Commands**: 20+
- **Documentation Pages**: 5
- **Code Lines**: 2000+
- **Language**: Python 3.7+

---

## 🔗 Links

- **GitHub Repository**: https://github.com/bio-computerinteranthusasum786/math-king-calculator
- **Calculator Functions**: [FUNCTIONS.md](FUNCTIONS.md)
- **To-Do List Guide**: [TODO_APP_GUIDE.md](TODO_APP_GUIDE.md)
- **API Reference**: [TODO_API_REFERENCE.md](TODO_API_REFERENCE.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)

---

## 🎉 Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/bio-computerinteranthusasum786/math-king-calculator.git
   cd math-king-calculator
   ```

2. **Install dependencies** (optional):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run calculator**:
   ```bash
   python calculator.py
   ```

4. **Run to-do list**:
   ```bash
   python todo_app.py
   ```

5. **Read documentation**:
   - Start with [TODO_APP_GUIDE.md](TODO_APP_GUIDE.md)
   - Explore [EXAMPLES.md](EXAMPLES.md)
   - Check [FUNCTIONS.md](FUNCTIONS.md) for calculator functions

---

## 💡 Tips

- Use `help` command in both applications for quick reference
- Tasks are automatically saved to `todos.json`
- Export tasks regularly for backup
- Explore the EXAMPLES.md for advanced workflows
- All 250+ calculator functions are documented in FUNCTIONS.md

---

## ✉️ Support

For issues, questions, or suggestions:
- Open a [GitHub Issue](https://github.com/bio-computerinteranthusasum786/math-king-calculator/issues)
- Check existing documentation
- Review examples for common use cases

---

**Made with ❤️ by [@bio-computerinteranthusasum786](https://github.com/bio-computerinteranthusasum786)**

**⭐ If you find this useful, please star the repository!**
