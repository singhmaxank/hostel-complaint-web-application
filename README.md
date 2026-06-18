# IILM Hostel Support Portal

## Overview
The **IILM Hostel Support Portal** is a lightweight, single-page web application (SPA) designed to streamline the process of logging and tracking hostel maintenance and support complaints. It provides a simple interface for students to report issues and a dedicated dashboard for hostel wardens and staff to track and resolve them efficiently.

## Features

### For Students
* **Easy Complaint Registration**: A clean, intuitive form to submit issues regarding rooms, facilities, or general hostel maintenance.
* **Detailed Reporting**: Capture specific details including roll number, hostel block, room number, and a thorough description of the issue.

### For Staff & Administration
* **Active Complaints Tracker**: A comprehensive tabular dashboard displaying all submitted tickets.
* **Status Management**: Real-time status updates (Pending 🔴, In Progress 🟡, Resolved 🟢) to keep track of maintenance workflows.
* **Quick Actions**: One-click buttons to update issue statuses without reloading the page.

## Tech Stack

* **Backend**: Python 3, Flask 3.0.0
* **Database**: SQLite3
* **Frontend**: HTML5, Vanilla JavaScript (Fetch API)
* **Styling**: Tailwind CSS (via CDN)
* **UI Components**: Feather Icons, SweetAlert2 (for interactive notifications)

## Project Structure

```text
├── app.py                     # Main Flask application and API routes
├── init_db.py                 # SQLite database initialization script
├── requirements.txt           # Python dependencies
├── static/
│   └── University_logostandard-BLUE-copy.png  # UI branding/logo
└── templates/
    └── index.html             # Main Single Page Application frontend
```
*(Note: Ensure your HTML file is named exactly `index.html` inside the `templates` folder for Flask to serve it correctly.)*

## Installation & Setup

Follow these steps to get the project running on your local machine:

**1. Clone the repository**
```bash
git clone https://github.com/singhmaxank/hostel-complaint-web-application.git
cd hostel-complaint-web-application
```

**2. Set up a virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Initialize the Database**
Run the database setup script to create the `complaints` table.
```bash
python init_db.py
```
*You should see a message: "✅ Database initialized successfully with new fields!"*

**5. Run the Application**
```bash
python app.py
```

**6. Access the Portal**
Open your web browser and navigate to: `http://127.0.0.1:5000`

## API Endpoints

The application exposes the following RESTful API endpoints:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Renders the main SPA interface. |
| `GET` | `/api/complaints` | Fetches all complaints ordered by newest first. |
| `POST` | `/api/complaints` | Creates a new complaint ticket. |
| `PATCH` | `/api/complaints/<id>` | Updates the status of a specific complaint. |

## Future Enhancements
* Implement secure user authentication and login sessions (JWT or Flask-Login).
* Add file upload support for students to attach images of the issues.
* Implement email notifications for students when their ticket status changes.
