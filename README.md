# innovation-i-challenge
A simple applications with two tables: the Employee table and a newly-created Task table.

## Backend Changes
**app/models/simple/task.py (new)**<br />
Pydantic validation model for sending and retrieving data through API endpoints

**app/routes/task.py (new)**<br />
Defines the APIs to retrieve, create, delete, and update rows in the Task table

**app/schemas/task.py (new)**<br />
Describes the schema of the Task table


## Frontend Changes
**components/TaskForm.vue (new)**<br />
To add new task or edit existing ones

**layouts/default.vue (modified)**<br />
Adds navigation functionality

**pages/index.vue (modified)**<br />
Implements a simple home page with app description and navigation buttons

**pages/task.vue (new)**<br />
Core logic for the Task page to display the table and relevant error message
