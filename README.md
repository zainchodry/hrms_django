# HRMS (Human Resource Management System)

A comprehensive Django-based Human Resource Management System designed to streamline employee management, attendance tracking, leave management, and payroll processing.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Apps](#project-apps)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionalities

- **User Authentication & Authorization**: Secure login system with role-based access control
- **Employee Management**: Complete employee profile management with department assignments
- **Attendance Tracking**: Track employee attendance with date-based records
- **Leave Management**: Request, approve, and manage employee leave applications
- **Payroll Processing**: Generate and manage employee payroll records
- **Department Management**: Organize employees by departments
- **Role-based Dashboards**: Separate dashboards for Admin, Managers, and Staff
- **User Profiles**: Manage user account and profile information

## Project Structure

```
hrms_django/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # Project documentation
├── accounts/                # User authentication and profiles
├── attendance/              # Attendance tracking system
├── dashboard/               # Dashboard views for different roles
├── departments/             # Department management
├── employees/               # Employee management
├── leaves/                  # Leave management system
├── payroll/                 # Payroll processing
├── hrms/                    # Main Django project settings
├── static/                  # Static files (CSS, JS, images)
├── staticfiles/             # Collected static files
└── templates/               # HTML templates
```

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite3

## Installation

### 1. Clone the Repository

```bash
git clone hrms_django.git
cd hrms_django
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## Configuration

The main Django settings are configured in `hrms/settings.py`. Key configurations include:

- **Database**: SQLite3 (default)
- **Installed Apps**: All project apps are registered in `INSTALLED_APPS`
- **Static Files**: Located in `static/` directory
- **Templates**: Located in `templates/` directory

## Running the Application

### Start Development Server

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`

### Access Admin Panel

Navigate to `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

## Usage

### Login

1. Navigate to the login page: `http://127.0.0.1:8000/accounts/login/`
2. Enter your credentials (email and password)
3. You'll be redirected to your role-specific dashboard

### User Roles

- **Admin**: Full access to all features and settings
- **Manager**: Can manage team attendance, leaves, and generate payroll reports
- **Staff**: Can view personal information, request leaves, and view attendance

### Dashboard Navigation

- **Admin Dashboard**: View system statistics and manage all resources
- **Manager Dashboard**: Manage team members and leave approvals
- **Staff Dashboard**: View personal information and request leaves

## Project Apps

### 1. **accounts** (`accounts/`)

Handles user authentication and profile management.

- **Models**: User registration, profile information
- **Views**: Login, logout, registration, profile management
- **Templates**: Login, register, profile pages

### 2. **employees** (`employees/`)

Manages employee information and details.

- **Models**: Employee profile, contact information
- **Views**: Employee list, employee details, edit profile
- **Forms**: Employee creation and update forms

### 3. **departments** (`departments/`)

Organizes employees into departments.

- **Models**: Department information
- **Views**: Department list, department details
- **Forms**: Department creation and management

### 4. **attendance** (`attendance/`)

Tracks employee attendance records.

- **Models**: Attendance records with date and status
- **Views**: Attendance list, mark attendance
- **Forms**: Attendance entry forms

### 5. **leaves** (`leaves/`)

Manages employee leave requests and approvals.

- **Models**: Leave requests, leave types, leave balances
- **Views**: Leave request form, leave history, leave management
- **Features**:
  - Submit leave requests
  - Approve/reject leave
  - Track leave balance
  - View leave history

### 6. **payroll** (`payroll/`)

Handles payroll processing and salary management.

- **Models**: Payroll records, salary information
- **Views**: Generate payroll, view payroll history
- **Utilities**: Payroll calculation functions

### 7. **dashboard** (`dashboard/`)

Provides role-specific dashboards.

- **Admin Dashboard**: System overview and statistics
- **Manager Dashboard**: Team management and reports
- **Staff Dashboard**: Personal information and requests

## Database Models

### Key Models

- **User**: Django built-in user model with extensions
- **Employee**: Employee information linked to User
- **Department**: Department organization
- **Attendance**: Daily attendance records
- **Leave**: Leave request tracking
- **Payroll**: Payroll records and calculations

### Relationships

- Employee → Department (ForeignKey)
- Employee → User (OneToOneField)
- Leave → Employee (ForeignKey)
- Attendance → Employee (ForeignKey)
- Payroll → Employee (ForeignKey)

## Admin Panel

The Django admin panel allows administrators to:

- Manage users and employees
- View and modify attendance records
- Review and process leave requests
- Generate and manage payroll
- Manage departments

Access via `/admin/` after logging in with superuser credentials.

## API Endpoints

### Authentication

- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout
- `POST /accounts/register/` - User registration

### Employees

- `GET /employees/` - List all employees
- `GET /employees/<id>/` - Get employee details

### Departments

- `GET /departments/` - List all departments
- `GET /departments/<id>/` - Get department details

### Attendance

- `GET /attendance/` - View attendance records
- `POST /attendance/` - Mark attendance

### Leaves

- `GET /leaves/my_leaves/` - View my leave requests
- `POST /leaves/` - Submit leave request
- `GET /leaves/manage_leaves/` - Manage leave requests (Manager)

### Payroll

- `GET /payroll/` - View payroll records
- `POST /payroll/generate/` - Generate payroll

## Static Files

CSS and JavaScript files are located in `static/` directory:

- `static/css/style.css` - Main stylesheet
- `static/images/` - Image assets
- `static/js/` - JavaScript files

Run the following command to collect static files for production:

```bash
python manage.py collectstatic
```

## Troubleshooting

### Database Issues

If you encounter database errors, reset the database:

```bash
# Delete existing database
rm db.sqlite3

# Run migrations
python manage.py migrate

# Create new superuser
python manage.py createsuperuser
```

### Migration Issues

If migrations fail, try:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Development Tips

- Use Django shell for testing: `python manage.py shell`
- Create superuser for admin access: `python manage.py createsuperuser`
- View SQL queries in development: Add `print()` statements in views
- Use Django debug toolbar for development (optional enhancement)

## Future Enhancements

- REST API for mobile app integration
- Advanced reporting and analytics
- Email notifications for leave approvals
- Integration with biometric attendance systems
- Performance management module
- Training and development module
- Document management system

## Contributing

To contribute to this project:

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## Security Notes

- Always use strong passwords for superuser accounts
- Keep Django updated to the latest stable version
- Use environment variables for sensitive configuration
- Enable HTTPS in production
- Configure ALLOWED_HOSTS in settings.py for production

## Support

For issues, questions, or suggestions, please create an issue in the project repository.

## License

This project is provided as-is for educational and organizational use.

---

**Last Updated**: February 6, 2026

For more information on Django, visit [Django Documentation](https://docs.djangoproject.com/)
