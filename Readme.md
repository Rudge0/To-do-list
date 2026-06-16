# To-do list

This is a small Django app for managing everyday tasks. It lets you create tasks, mark them as completed, set deadlines, and attach tags so the list stays organized.

It feels like a learning project or an early pet project, but it already has the core pieces in place: CRUD operations, pagination, and a clean enough structure to keep building on.

## What it does

- create, update, and delete tasks;
- switch task status between done and not done;
- store a short description, creation date, and deadline;
- assign tags to tasks;
- manage tags on a separate page;
- paginate task and tag lists;
- render forms with `django-crispy-forms` and `Bootstrap 4`.

## Tech stack

- Python 3
- Django 6
- SQLite
- Bootstrap 4
- django-crispy-forms

## Running locally

1. Clone the repository:

```bash
git clone <your-repo-url>
cd To-do-list
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Then open:

`http://127.0.0.1:8000/`

## How to use it

- the home page shows the task list;
- `Create task` opens the form for a new task;
- `Complete` and `Undo` toggle the task status;
- each task has `Update` and `Delete` actions;
- the `Tags` page is used to create, edit, and delete tags.

## Project structure

```text
To-do-list/
├── list/                # main app: models, views, urls
├── templates/           # HTML templates
├── static/              # custom CSS
├── to_do_list/          # Django project settings
├── db.sqlite3           # local database
├── manage.py
└── requirements.txt
```

## Models

### `Tag`

Stores a tag name and is used to group related tasks.

### `Task`

Contains:

- `name`
- `description`
- `done`
- `created_at`
- `deadline`
- a `ManyToMany` relationship with tags

## What could be improved

There are a few obvious next steps if this project keeps growing:

- add filtering by status or tag;
- add search;
- move form configuration into `forms.py`;
- add tests, since coverage is basically missing right now;
- remove unfinished or placeholder views if they are no longer needed;
- prepare the project for deployment with proper `ALLOWED_HOSTS`, `DEBUG=False`, and environment variables.

## Note

The repository already includes `db.sqlite3`, so after migrations the app can be started locally right away. If you want a clean start, you can recreate or replace the database file.
