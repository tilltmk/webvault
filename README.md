# WebVault App 🗃️

WebVault is a Flask-based web application for archiving websites. Users can save websites, manage versions, and generate websites as PDFs.

## Structure 📂

```
WebVault/
│
├── app/
│   ├── static/
│   │   └── script.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── website_view.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── archived_websites/
├── config.py
├── requirements.txt
└── run.py
```

## Key Files 📑

- `app/__init__.py`: Initializes the Flask app and configures the database.
- `app/models.py`: Defines the database models.
- `app/routes.py`: Defines the routes and views.
- `app/utils.py`: Helper functions for downloading and saving websites.
- `app/templates/`: HTML templates for the user interface.

## Features 🔍

- 🔐 User login and registration.
- 🌐 Adding and saving URLs.
- 📁 Downloading and saving websites.
- 🔄 Website versioning.
- 📊 Overview page with all archived URLs.
- 🖥️ Browsing archived websites.
- 📄 Saving websites as PDFs.

## Design 🎨

- Responsive layout using Bootstrap 5.3.
- Adjustments for mobile screens.
- Color scheme: Matte green with dark background.

## Prerequisites 🛠️

- Flask
- Flask-SQLAlchemy
- Flask-Login
- requests
- beautifulsoup4
- WeasyPrint

## Installation on Windows 🖥️

1. Install MSYS2 from the [MSYS2 website](https://www.msys2.org/).
2. Execute the following commands in the MSYS2 console:
   ```
   pacman -Syu
   pacman -S mingw-w64-x86_64-gtk3
   ```
3. Add `C:\msys64\mingw64\bin` to your `PATH`.
4. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

## Installation on Linux 🐧

Follow these steps to set up WebVault on a Linux system:

1. **Install Dependencies**:
   - First, ensure that you have Python and pip installed. You can install them using your package manager. For Ubuntu, you might use:
     ```
     sudo apt update
     sudo apt install python3 python3-pip
     ```
   - Install GTK for WeasyPrint:
     ```
     sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
     ```

2. **Clone the Repository**:
   - Clone the WebVault repository from GitHub:
     ```
     git clone https://github.com/tilltmk/webvault
     cd WebVault
     ```

3. **Setup a Python Virtual Environment** (recommended):
   - Create and activate a virtual environment:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Python Dependencies**:
   - Install the required Python packages using pip:
     ```
     pip install -r requirements.txt
     ```

5. **Configure Environment Variables**:
   - Set up necessary environment variables, such as `FLASK_APP` and `FLASK_ENV`, and any other configurations specific to your setup.

6. **Initialize the Database**:
   - Run the initialization script provided in the repository to set up your database schemas:
     ```
     python run.py init_db
     ```

7. **Run the Application**:
   - Start the Flask application:
     ```
     flask run
     ```

Visit `http://localhost:5000` in your web browser to start using WebVault.
