# 📚 To-Do List Application - API Reference

## Class: TodoItem

Represents a single to-do item.

### Constructor

```python
TodoItem(
    title: str,
    description: str = "",
    priority: str = "medium",
    due_date: Optional[str] = None,
    task_id: Optional[str] = None,
    completed: bool = False,
    created_at: Optional[str] = None,
    completed_at: Optional[str] = None,
    tags: Optional[List[str]] = None,
)
```

### Methods

#### `mark_complete()`
Mark the task as completed.

```python
task.mark_complete()
```

#### `mark_incomplete()`
Mark the task as incomplete.

```python
task.mark_incomplete()
```

#### `to_dict()`
Convert task to dictionary.

```python
task_dict = task.to_dict()
# Returns: {
#     "id": "...",
#     "title": "...",
#     "description": "...",
#     "priority": "medium",
#     "due_date": "2026-07-05",
#     "completed": False,
#     "created_at": "2026-06-30T...",
#     "completed_at": None,
#     "tags": [...]
# }
```

#### `from_dict(data)`
Create TodoItem from dictionary.

```python
task = TodoItem.from_dict({
    "id": "abc123",
    "title": "Buy milk",
    "priority": "medium"
})
```

---

## Class: TodoList

Manages a collection of to-do items with local storage.

### Constructor

```python
TodoList(storage_file: str = "todos.json")
```

**Parameters:**
- `storage_file` (str): Path to JSON file for persistence

**Example:**
```python
todo_list = TodoList("my_todos.json")
```

---

## File Operations

### `load_from_storage() -> bool`
Load tasks from local storage.

```python
success = todo_list.load_from_storage()
if success:
    print(f"Loaded {len(todo_list.tasks)} tasks")
```

### `save_to_storage() -> bool`
Save tasks to local storage.

```python
if todo_list.save_to_storage():
    print("Tasks saved successfully")
```

### `export_to_file(filename: str) -> bool`
Export tasks to a specific file.

```python
todo_list.export_to_file("backup.json")
```

### `import_from_file(filename: str) -> bool`
Import tasks from a file.

```python
todo_list.import_from_file("backup.json")
```

---

## CRUD Operations

### `add_task(title, description, priority, due_date, tags) -> TodoItem`
Add a new task.

```python
task = todo_list.add_task(
    title="Buy milk",
    description="1 liter whole milk",
    priority="medium",
    due_date="2026-07-05",
    tags=["shopping", "groceries"]
)
print(f"Task added with ID: {task.id}")
```

### `get_task(task_id: str) -> Optional[TodoItem]`
Get a specific task by ID.

```python
task = todo_list.get_task("abc123")
if task:
    print(task.title)
```

### `get_all_tasks() -> List[TodoItem]`
Get all tasks.

```python
all_tasks = todo_list.get_all_tasks()
print(f"Total tasks: {len(all_tasks)}")
```

### `update_task(task_id, title, description, priority, due_date, tags) -> bool`
Update an existing task.

```python
success = todo_list.update_task(
    task_id="abc123",
    title="Buy milk and bread",
    priority="high"
)
```

### `delete_task(task_id: str) -> bool`
Delete a specific task.

```python
if todo_list.delete_task("abc123"):
    print("Task deleted")
```

### `delete_all_tasks() -> int`
Delete all tasks.

```python
count = todo_list.delete_all_tasks()
print(f"Deleted {count} tasks")
```

---

## Task Management

### `complete_task(task_id: str) -> bool`
Mark a task as completed.

```python
if todo_list.complete_task("abc123"):
    print("Task completed")
```

### `uncomplete_task(task_id: str) -> bool`
Mark a task as incomplete.

```python
if todo_list.uncomplete_task("abc123"):
    print("Task marked incomplete")
```

### `toggle_task(task_id: str) -> bool`
Toggle task completion status.

```python
if todo_list.toggle_task("abc123"):
    task = todo_list.get_task("abc123")
    print(f"Toggled to: {task.completed}")
```

---

## Filtering & Search

### `get_completed_tasks() -> List[TodoItem]`
Get all completed tasks.

```python
completed = todo_list.get_completed_tasks()
print(f"Completed: {len(completed)} tasks")
```

### `get_pending_tasks() -> List[TodoItem]`
Get all incomplete tasks.

```python
pending = todo_list.get_pending_tasks()
for task in pending:
    print(task.title)
```

### `get_tasks_by_priority(priority: str) -> List[TodoItem]`
Get tasks by priority level.

```python
high_priority = todo_list.get_tasks_by_priority("high")
for task in high_priority:
    print(f"HIGH: {task.title}")
```

### `get_tasks_by_tag(tag: str) -> List[TodoItem]`
Get tasks by tag.

```python
shopping = todo_list.get_tasks_by_tag("shopping")
for task in shopping:
    print(f"SHOPPING: {task.title}")
```

### `search_tasks(query: str) -> List[TodoItem]`
Search tasks by title or description.

```python
results = todo_list.search_tasks("milk")
for task in results:
    print(f"FOUND: {task.title}")
```

### `get_overdue_tasks() -> List[TodoItem]`
Get tasks that are past their due date.

```python
overdue = todo_list.get_overdue_tasks()
print(f"Overdue: {len(overdue)} tasks")
```

### `get_tasks_due_today() -> List[TodoItem]`
Get tasks due today.

```python
today = todo_list.get_tasks_due_today()
for task in today:
    print(f"DUE TODAY: {task.title}")
```

### `get_tasks_due_soon(days: int = 7) -> List[TodoItem]`
Get tasks due within N days.

```python
week = todo_list.get_tasks_due_soon(7)
for task in week:
    print(f"DUE THIS WEEK: {task.title}")
```

---

## Statistics

### `get_statistics() -> Dict[str, Any]`
Get task statistics.

```python
stats = todo_list.get_statistics()
print(f"Total: {stats['total_tasks']}")
print(f"Completed: {stats['completed']}")
print(f"Pending: {stats['pending']}")
print(f"Completion Rate: {stats['completion_rate']}")
print(f"Overdue: {stats['overdue']}")
print(f"Due Today: {stats['due_today']}")
print(f"Priority Breakdown: {stats['priority_breakdown']}")
```

### `clear_completed_tasks() -> int`
Remove all completed tasks.

```python
count = todo_list.clear_completed_tasks()
print(f"Removed {count} completed tasks")
```

---

## Display Methods

### `display_all_tasks(show_completed: bool = True) -> None`
Display all tasks in formatted output.

```python
todo_list.display_all_tasks()
todo_list.display_all_tasks(show_completed=False)  # Only pending
```

### `display_statistics() -> None`
Display task statistics in formatted output.

```python
todo_list.display_statistics()
```

---

## Complete Example

```python
from todo_app import TodoList

# Create instance
todo_list = TodoList("my_tasks.json")

# Add tasks
task1 = todo_list.add_task(
    title="Learn Python",
    description="Complete online course",
    priority="high",
    due_date="2026-08-01",
    tags=["learning", "python"]
)

task2 = todo_list.add_task(
    title="Buy groceries",
    priority="medium",
    due_date="2026-07-05",
    tags=["shopping"]
)

# Display all tasks
todo_list.display_all_tasks()

# Get statistics
stats = todo_list.get_statistics()
print(f"Completion rate: {stats['completion_rate']}")

# Complete first task
todo_list.complete_task(task1.id)

# Get pending tasks
pending = todo_list.get_pending_tasks()
print(f"Pending: {len(pending)} tasks")

# Export to backup
todo_list.export_to_file("backup.json")

# Import from backup
todo_list.import_from_file("backup.json")

# Display statistics
todo_list.display_statistics()
```

---

## Error Handling

All methods include error handling:

```python
try:
    task = todo_list.add_task(title="")
except ValueError as e:
    print(f"Error: {e}")  # Task title cannot be empty

try:
    success = todo_list.save_to_storage()
except IOError as e:
    print(f"Error saving: {e}")
```

---

## Data Persistence

Tasks are automatically saved to JSON:

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Learn Python",
    "description": "Complete online course",
    "priority": "high",
    "due_date": "2026-08-01",
    "completed": false,
    "created_at": "2026-06-30T12:30:45.123456",
    "completed_at": null,
    "tags": ["learning", "python"]
  }
]
```

---

## Performance Notes

- All tasks are loaded into memory on initialization
- Modifications trigger automatic file save
- Suitable for up to thousands of tasks
- JSON format is human-readable and portable

---

For interactive usage, see [TODO_APP_GUIDE.md](TODO_APP_GUIDE.md)
