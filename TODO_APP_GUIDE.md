# 📝 To-Do List Application - Complete Guide

## Overview

A powerful and user-friendly to-do list application with **local storage** functionality. All tasks are automatically saved to a JSON file for persistence.

## 🚀 Quick Start

### Installation

No additional dependencies needed! The app uses only Python standard library.

```bash
python todo_app.py
```

### First Run

```
============================================================
✅ WELCOME TO TO-DO LIST APPLICATION
============================================================
Type 'help' for available commands or 'quit' to exit

> help
```

## 📋 Commands Reference

### Basic Operations

#### `add <title>`
Add a new task to your list

```
> add Buy groceries
  Description (optional): Milk, eggs, bread
  Priority [low/medium/high/urgent] (default: medium): medium
  Due date (YYYY-MM-DD, optional): 2026-07-05
  Tags (comma-separated, optional): shopping, errands

✅ Task added: Buy groceries (ID: abc123...)
```

#### `list`
Display all tasks

```
> list
================================================================================
📋 TO-DO LIST
================================================================================
1. ○ [🟡] Buy groceries (Due: 2026-07-05) #shopping, #errands
   Description: Milk, eggs, bread
   ID: abc123def456

2. ✓ [🟢] Complete project report
   Description: Quarterly report
   ID: xyz789abc123
```

#### `list-pending`
Show only incomplete tasks

```
> list-pending
============================================================
📝 PENDING TASKS
============================================================
1. ○ [🟡] Buy groceries (Due: 2026-07-05) #shopping
```

#### `list-completed`
Show only completed tasks

```
> list-completed
============================================================
✅ COMPLETED TASKS
============================================================
1. ✓ [🟢] Complete project report
```

---

### Task Management

#### `complete <id>`
Mark a task as completed

```
> complete abc123def456
✅ Task marked as completed
```

#### `uncomplete <id>`
Mark a task as incomplete

```
> uncomplete abc123def456
↩️  Task marked as incomplete
```

#### `toggle <id>`
Toggle task between completed and incomplete

```
> toggle abc123def456
🔄 Task toggled to completed
```

#### `delete <id>`
Delete a specific task

```
> delete abc123def456
🗑️  Task deleted
```

#### `delete-all`
Delete all tasks (with confirmation)

```
> delete-all
  ⚠️  Are you sure? (yes/no): yes
🗑️  Deleted 5 tasks
```

#### `clear-completed`
Remove all completed tasks

```
> clear-completed
✨ Cleared 2 completed tasks
```

---

### Filtering & Search

#### `priority <level>`
Get tasks by priority level (low, medium, high, urgent)

```
> priority high
HIGH PRIORITY TASKS:
1. ○ [🔴] Fix critical bug
2. ○ [🔴] Client meeting prep
```

#### `tag <name>`
Get all tasks with a specific tag

```
> tag shopping
TASKS WITH TAG '#shopping':
1. ○ [🟡] Buy groceries
2. ○ [🟡] Shop for supplies
```

#### `search <query>`
Search tasks by title or description

```
> search report
SEARCH RESULTS FOR 'report':
1. ✓ [🟢] Complete project report
2. ○ [🟡] Review monthly report
```

#### `overdue`
Show tasks that are past their due date

```
> overdue
============================================================
⏰ OVERDUE TASKS
============================================================
1. ○ [🔴] Submit expenses (Due: 2026-06-25)
```

#### `today`
Show tasks due today

```
> today
============================================================
📅 DUE TODAY
============================================================
1. ○ [🟡] Team standup meeting (Due: 2026-06-30)
```

#### `week`
Show tasks due within the next 7 days

```
> week
============================================================
📆 DUE THIS WEEK
============================================================
1. ○ [🟡] Team standup meeting (Due: 2026-06-30)
2. ○ [🟡] Buy groceries (Due: 2026-07-02)
```

---

### Statistics & Information

#### `stats`
Display comprehensive task statistics

```
> stats

============================================================
📊 TASK STATISTICS
============================================================
Total Tasks: 10
Completed: 3
Pending: 7
Completion Rate: 30.0%
Overdue: 1
Due Today: 2

Priority Breakdown:
  Low: 2
  Medium: 5
  High: 2
  Urgent: 1
============================================================
```

#### `export <filename>`
Export all tasks to a JSON file

```
> export my_tasks_backup.json
✅ Tasks exported to my_tasks_backup.json
```

#### `import <filename>`
Import tasks from a JSON file

```
> import my_tasks_backup.json
✅ Tasks imported from my_tasks_backup.json
```

---

## 💾 Local Storage

### Auto-Save
All changes are automatically saved to `todos.json` in the same directory. No need to manually save!

### File Format
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "priority": "medium",
    "due_date": "2026-07-05",
    "completed": false,
    "created_at": "2026-06-30T12:30:45.123456",
    "completed_at": null,
    "tags": ["shopping", "errands"]
  }
]
```

### Backup & Recovery

Your tasks are stored in `todos.json`. You can:
- **Back it up**: Copy `todos.json` to a safe location
- **Restore**: Copy it back to the application directory
- **Share**: Email `todos.json` to sync across devices
- **Archive**: Keep multiple versions with timestamps

---

## 🎯 Usage Examples

### Example 1: Project Management
```
> add Design homepage
  Description: Create mockups and design system
  Priority: high
  Due date: 2026-07-10
  Tags: design, project-alpha

> add Implement authentication
  Priority: urgent
  Due date: 2026-07-08
  Tags: development, security, project-alpha

> add Write API documentation
  Priority: medium
  Due date: 2026-07-15
  Tags: documentation, project-alpha
```

### Example 2: Personal Errands
```
> add Grocery shopping
  Priority: medium
  Tags: shopping, home

> add Pay bills
  Priority: high
  Tags: finance

> add Car maintenance
  Priority: medium
  Tags: car, home
```

### Example 3: Workflow
```
# Add tasks
> add Fix login bug
  Priority: urgent
  Tags: bugs, critical

# List pending
> list-pending

# Work on task and complete
> complete <id>

# Review stats
> stats

# Export for backup
> export weekly_backup.json
```

---

## 🎨 Priority Levels

| Priority | Emoji | Use Case |
|----------|-------|----------|
| 🟢 Low | 🟢 | Can wait, nice to have |
| 🟡 Medium | 🟡 | Regular tasks, normal importance |
| 🔴 High | 🔴 | Important, deadline soon |
| 🔴🔴 Urgent | 🔴🔴 | Critical, do immediately |

---

## 📊 Task Status Indicators

| Symbol | Meaning |
|--------|----------|
| ○ | Incomplete task |
| ✓ | Completed task |

---

## 🔍 Tips & Tricks

### Organize with Tags
Use tags to categorize tasks:
```
> tag work
> tag home
> tag shopping
> tag urgent
```

### Use Priority Levels Effectively
- **Urgent**: Do today (🔴🔴)
- **High**: Do this week (🔴)
- **Medium**: Do this month (🟡)
- **Low**: Backlog (🟢)

### Regular Cleanup
```
> stats          # Check progress
> clear-completed  # Remove done items
> overdue        # Handle past deadlines
```

### Quick Review Workflow
```
> today          # What's due today?
> week           # What's this week?
> overdue        # What's late?
> stats          # How am I doing?
```

---

## 🐛 Troubleshooting

### Tasks not saving?
- Check file permissions on `todos.json`
- Ensure you have write access to the directory
- Try exporting to a different location

### Can't import tasks?
- Verify JSON file format is correct
- Ensure file exists in the application directory
- Check that the file contains valid task data

### Lost tasks?
- Check if `todos.json` exists
- Look for backup files you may have created
- Tasks are automatically saved after each operation

---

## 💡 Advanced Features

### Python API

Use the TodoList class programmatically:

```python
from todo_app import TodoList, TodoItem

# Create instance
todo_list = TodoList()

# Add task
task = todo_list.add_task(
    title="Learn Python",
    description="Complete advanced Python course",
    priority="high",
    due_date="2026-07-15",
    tags=["learning", "python"]
)

# Get statistics
stats = todo_list.get_statistics()
print(f"Completion rate: {stats['completion_rate']}")

# Filter tasks
pending = todo_list.get_pending_tasks()
high_priority = todo_list.get_tasks_by_priority("high")

# Export/Import
todo_list.export_to_file("backup.json")
todo_list.import_from_file("backup.json")
```

---

## 📝 File Structure

```
math-king-calculator/
├── calculator.py          # Scientific calculator
├── todo_app.py           # To-do list app (NEW!)
├── todos.json            # Auto-generated storage
├── README.md
├── FUNCTIONS.md
├── TODO_APP_GUIDE.md     # This file
└── requirements.txt
```

---

## 🎓 Getting Started

1. **Run the app**: `python todo_app.py`
2. **Type `help`**: See all available commands
3. **Add your first task**: `add My first task`
4. **Complete it**: `complete <task-id>`
5. **Check stats**: `stats`
6. **Enjoy!** ✨

---

**Happy task managing!** 🚀
