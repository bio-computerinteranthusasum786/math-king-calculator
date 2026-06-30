# 📚 To-Do List Application - Practical Examples

## Getting Started

### Run the Application

```bash
python todo_app.py
```

You'll see:
```
============================================================
✅ WELCOME TO TO-DO LIST APPLICATION
============================================================
Type 'help' for available commands or 'quit' to exit

>
```

---

## Example 1: Daily Task Management

### Scenario
You want to organize your daily tasks.

### Commands

```bash
# Add morning tasks
> add Morning standup
  Description: Team sync at 9 AM
  Priority: high
  Due date: 2026-06-30
  Tags: work, meetings

> add Check emails
  Priority: medium
  Tags: work

> add Coffee break
  Priority: low
  Tags: break

# View all pending tasks
> list-pending

# Mark standup as completed
> complete <task-id>

# View remaining tasks
> list-pending

# Check daily stats
> stats
```

### Result
All tasks are saved automatically to `todos.json`

---

## Example 2: Project-Based Organization

### Scenario
Manage tasks for a web development project.

### Commands

```bash
# Project setup
> add Design database schema
  Description: Plan user, product, order tables
  Priority: high
  Due date: 2026-07-05
  Tags: database, project-web

> add Create API endpoints
  Description: User auth, products, orders
  Priority: high
  Due date: 2026-07-10
  Tags: backend, api, project-web

> add Build frontend UI
  Description: React components
  Priority: medium
  Due date: 2026-07-15
  Tags: frontend, react, project-web

> add Write tests
  Description: Unit and integration tests
  Priority: high
  Due date: 2026-07-20
  Tags: testing, project-web

> add Deploy to production
  Description: Set up CI/CD pipeline
  Priority: medium
  Due date: 2026-07-25
  Tags: devops, project-web

# View all project tasks
> tag project-web

# See high priority items
> priority high

# Complete a task
> complete <task-id>

# Track progress
> stats

# Export project tasks
> export web-project-tasks.json
```

---

## Example 3: Personal Life Organization

### Scenario
Manage work, health, and personal tasks.

### Commands

```bash
# Work tasks
> add Prepare quarterly report
  Priority: high
  Due date: 2026-07-05
  Tags: work, reports

> add Review team performance
  Priority: medium
  Due date: 2026-07-10
  Tags: work, management

# Health tasks
> add Doctor appointment
  Description: Annual checkup with Dr. Smith
  Priority: high
  Due date: 2026-07-03
  Tags: health, medical

> add Gym membership renewal
  Priority: low
  Due date: 2026-07-20
  Tags: health, fitness

# Personal tasks
> add Fix leaky faucet
  Priority: medium
  Due date: 2026-07-15
  Tags: home, maintenance

> add Buy birthday gift
  Description: For Sarah, budget $50
  Priority: medium
  Due date: 2026-07-08
  Tags: personal, shopping

# View by category
> tag work
> tag health
> tag personal

# Check what's due today
> today

# Check what's coming up
> week

# Complete a task
> complete <task-id>
```

---

## Example 4: Using Priority Levels

### Scenario
Effectively use priority levels.

### Commands

```bash
# 🔴 URGENT (Do immediately)
> add Fix production bug
  Priority: urgent
  Tags: critical, bugs

# 🔴 HIGH (Do this week)
> add Design new feature
  Priority: high
  Due date: 2026-07-05
  Tags: features

# 🟡 MEDIUM (Do this month)
> add Code review
  Priority: medium
  Due date: 2026-07-15
  Tags: team

# 🟢 LOW (Backlog)
> add Learn new tool
  Priority: low
  Tags: learning

# View by priority
> priority urgent
> priority high
> priority medium
> priority low
```

---

## Example 5: Search and Filter

### Scenario
Find specific tasks quickly.

### Commands

```bash
# First, add various tasks
> add "Research market trends"
> add "Attend marketing meeting"
> add "Plan marketing campaign"
> add "Write blog post"
> add "Design banner"

# Search for tasks containing "market"
> search market
RESULT:
1. Research market trends
2. Attend marketing meeting
3. Plan marketing campaign

# Search for tasks containing "design"
> search design
RESULT:
1. Design banner

# Search for tasks containing "write"
> search write
RESULT:
1. Write blog post

# Filter by tag
> tag marketing

# Find urgent tasks
> priority urgent
```

---

## Example 6: Deadline Management

### Scenario
Stay on top of deadlines.

### Commands

```bash
# Add tasks with different deadlines
> add "Submit proposal"
  Due date: 2026-06-28  # Past deadline

> add "Approve budget"
  Due date: 2026-06-30  # Today

> add "Send invoice"
  Due date: 2026-07-02  # Soon

> add "Plan vacation"
  Due date: 2026-07-10  # Next week

# Check overdue tasks
> overdue
OVERDUE TASKS:
1. Submit proposal (Due: 2026-06-28) ⏰

# Check today's tasks
> today
DUE TODAY:
1. Approve budget (Due: 2026-06-30) 📅

# Check upcoming week
> week
DUE THIS WEEK:
1. Send invoice (Due: 2026-07-02)
2. Plan vacation (Due: 2026-07-10)

# Handle overdue tasks
> complete <task-id>  # Complete it
# OR
> update <task-id>   # Reschedule it
```

---

## Example 7: Backup and Import

### Scenario
Safely back up your tasks and move between devices.

### Commands

```bash
# Create a backup
> export my_tasks_backup_2026-06-30.json
✅ Tasks exported to my_tasks_backup_2026-06-30.json

# Add more tasks
> add New task 1
> add New task 2

# Export again
> export weekly_backup.json

# View your backups
# File system shows:
# - todos.json (current)
# - my_tasks_backup_2026-06-30.json (backup)
# - weekly_backup.json (backup)

# Import from backup (if needed)
> import my_tasks_backup_2026-06-30.json
✅ Tasks imported from my_tasks_backup_2026-06-30.json

# Share tasks with someone
> export shared_project.json
# Send file to colleague
# Colleague imports:
> import shared_project.json
```

---

## Example 8: Weekly Planning

### Scenario
Plan your week systematically.

### Commands

```bash
# Monday
> add "Review previous week"
  Priority: medium
  Due date: 2026-07-01
  Tags: planning, weekly

> add "Plan this week"
  Priority: high
  Due date: 2026-07-01
  Tags: planning, weekly

# Add weekly tasks
> add "Weekly team meeting"
  Priority: high
  Due date: 2026-07-01
  Tags: meetings, weekly

> add "Update progress tracker"
  Priority: medium
  Due date: 2026-07-05
  Tags: admin, weekly

# Tuesday to Friday - specific tasks
> add "Feature development"
  Priority: high
  Due date: 2026-07-03
  Tags: development

> add "Code review"
  Priority: medium
  Due date: 2026-07-04
  Tags: code-review

# Friday - wrap up
> add "Prepare weekly report"
  Priority: high
  Due date: 2026-07-05
  Tags: reports

# View week's tasks
> week

# Check daily
> today

# End of week - archive
> complete <all-completed-ids>
> stats
> export weekly_report.json
```

---

## Example 9: Cleaning Up

### Scenario
Keep your to-do list clean.

### Commands

```bash
# Check current status
> stats
Total Tasks: 50
Completed: 35
Pending: 15

# View all completed
> list-completed

# Remove completed tasks
> clear-completed
✨ Cleared 35 completed tasks

# Check status again
> stats
Total Tasks: 15
Completed: 0
Pending: 15

# Backup before cleanup
> export archive_completed.json
```

---

## Example 10: Complete Workflow

### Scenario
Full day workflow.

### Commands

```bash
# Morning - check priorities
> today
> priority urgent
> stats

# Work on tasks
> list-pending
> complete <task-id>  # Completed first task
> complete <task-id>  # Completed second task

# Mid-day - check progress
> stats

# Add urgent task
> add "Handle client issue"
  Priority: urgent
  Tags: urgent, client

# Search for related tasks
> search client
> tag client

# Complete urgent task
> complete <task-id>

# End of day - review
> stats
> list-pending
> overdue  # Any missed deadlines?
> clear-completed

# Backup before closing
> export daily_backup_2026-06-30.json

# Exit
> quit
```

---

## Python Script Usage

### Example: Automated Task Creation

```python
from todo_app import TodoList
from datetime import datetime, timedelta

# Create instance
todo_list = TodoList()

# Add weekly recurring tasks
weekly_tasks = [
    ("Monday Standup", "Team sync at 9 AM", "high"),
    ("Code Review", "Review team PRs", "medium"),
    ("Weekly Report", "Summarize progress", "high"),
    ("Planning", "Plan next sprint", "medium"),
]

for i, (title, desc, priority) in enumerate(weekly_tasks):
    due_date = (datetime.now() + timedelta(days=i+1)).date().isoformat()
    todo_list.add_task(
        title=title,
        description=desc,
        priority=priority,
        due_date=due_date,
        tags=["weekly", "recurring"]
    )

print("Weekly tasks created!")
todo_list.display_all_tasks()
```

### Example: Statistics Report

```python
from todo_app import TodoList

todo_list = TodoList()
stats = todo_list.get_statistics()

print("\n📊 Weekly Report")
print(f"Total tasks: {stats['total_tasks']}")
print(f"Completed: {stats['completed']}")
print(f"Completion rate: {stats['completion_rate']}")
print(f"Overdue: {stats['overdue']}")
print(f"\nPriority Breakdown:")
for priority, count in stats['priority_breakdown'].items():
    print(f"  {priority.capitalize()}: {count}")
```

---

Start using these examples and customize them for your workflow! 🚀
