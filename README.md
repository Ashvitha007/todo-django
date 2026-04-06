Todo App – Django

A simple and clean **Todo List Web Application** built with **Python** and **Django**. Create, manage, and track your daily tasks with ease.

---

Features

- Add new tasks
- View all tasks in a list
- Mark tasks as complete / incomplete
- Delete tasks
- Clean and minimal UI

---

Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend language |
| Django | Web framework |
| SQLite | Default database |
| HTML/CSS | Frontend templates |

---

📁 Project Structure

```
todo-django/
├── todo/               # Main Django app
│   ├── models.py       # Task model
│   ├── views.py        # App logic
│   ├── urls.py         # URL routing
│   └── templates/      # HTML templates
├── requirements.txt    # Python dependencies
└── manage.py           # Django management script
```

---

 Installation & Setup

 1. Clone the repository

```bash
git clone https://github.com/Ashvitha007/todo-django.git
cd todo-django
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

 3. Install dependencies

```bash
pip install -r requirements.txt
```

 4. Run database migrations

```bash
python manage.py migrate
```

 5. Start the development server

```bash
python manage.py runserver
```

### 6. Open in browser

```
http://127.0.0.1:8000/
```

Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

 License

This project is open source.

---

Made with [Ashvitha007](https://github.com/Ashvitha007)
