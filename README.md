# QR Vault Pro

A professional-grade, multi-user QR code generator and management system. This application uses a modular Flask backend, a relational SQLite database, and a decoupled frontend with persistent user tracking via local browser identification.

## 📂 Project Structure

```
qr-vault-pro/
├── vercel.json         # Vercel development configuration
├── app.py              # Main entry point; initializes Flask & Database
├── config.py           # Application configurations & environment settings
├── models.py           # SQLAlchemy Database models (Users & QRRecords)
├── routes.py           # API Blueprint containing all functional end points 
├── requirements.txt    # Python dependency list
├── .gitignore          # Git ignore file to exclude instance folder and other unwanted files
├── instance/           # Generated automatically (contains qr_vault.db)
├── static/             # Static assets
│   ├── css/
│   │   └── style.css   # Custom UI styling and animations
│   └── js/
│       └── script.js   # Client-side logic, API calls, and QR rendering
└── templates/          # Jinja2 HTML templates
    └── index.html      # Main Dashboard interface
```

## 🚀 Key Features

- **Modular Architecture**: Clean separation of concerns between data models, routing logic, and application configuration.
- **Multi-User Persistence**: Automatically generates a unique user_id stored in local Storage. History is filtered server-side to ensure privacy.
- **Relational Database**: Uses SQLite with Flask-SQLAlchemy to manage the relationship between users and their generated records.
- **Client-Side Rendering**: High-speed QR generation using qrcode.js to minimize server overhead.
- **Full CRUD Logic**: Users can create, view, download (PNG), and delete their history.
- **Modern UI**: Built with Tailwind CSS, featuring responsive layouts, custom scrollbars, and toast notifications.

## 🛠️ Installation & Setup

1. Clone the repository (or save the files into the structure shown above).
2. Install dependencies (recommended to use a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize & Run:
   ```bash
   python app.py
   ```
4. Access the app at `http://127.0.0.1:5000`

## 📊 Database Schema

### Users Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary Key |
| unique_id | String | Browser-generated UUID |
| created_at | DateTime | Timestamp of first visit |

### QR Records Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary Key |
| content | Text | The encoded text or URL |
| user_id | Integer | Foreign Key linking to users.id |
| created_at | DateTime | Timestamp of generation |

## 🛡️ Security & Scalability

- **Input Validation**: API endpoints enforce content checks and length limits.
- **ORM Protection**: Using SQLAlchemy prevents SQL Injection attacks by using parameterized queries automatically.
- **Blueprint Pattern**: The API is registered as a Flask Blueprint, allowing for easy scaling (e.g., adding an admin panel or authentication module in the future).
