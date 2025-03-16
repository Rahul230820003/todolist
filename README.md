# TodoList

TodoList is a simple web application built with Django that allows users to manage their daily tasks efficiently. This application provides a user-friendly interface to add, update, and delete tasks.

## Features

- Add new tasks with a title and description.
- Update existing tasks.
- Delete tasks that are no longer needed.
- View all tasks in a list format.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd todolist
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- `todo_app/`: Contains the main application code including models, views, and templates.
- `manage.py`: A command-line utility that lets you interact with this Django project.
- `db.sqlite3`: The SQLite database file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.


