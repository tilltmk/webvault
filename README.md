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
