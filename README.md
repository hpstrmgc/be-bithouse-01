# Be-Bithouse-01

## Overview
Be-Bithouse-01 is a simple Django application that uses PostgreSQL as its database. The project includes features such as employee management and certification tracking.

---

## Installation and Setup Guide

### Prerequisites
- Python 3.x
- PostgreSQL
- Git

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/hpstrmgc/be-bithouse-01.git
```

#### 2. Navigate to Project Directory
```bash
cd be-bithouse-01
```

#### 3. Create and Activate Virtual Environment

Create a virtual environment to manage dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Configure Environment Variables
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

#### 6. Run Database Migrations
```bash
python manage.py migrate
```

#### 7. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Usage

### Accessing Employee Data
To access employee data, navigate to:
```
http://127.0.0.1:8000/employeeapp/employee/{employee-id}/
```

## API Endpoints

Below are the endpoints available in this application:

### Main Endpoints
- `GET /` - Application index page

### Employee Endpoints
- `GET /employee/<int:employee_id>/` - Display employee details and certifications
- `POST /employee/<int:employee_id>/` - Update employee data (via edit form)

### Certification Endpoints
- `POST /add-certification/` - Add a new certification for an employee
- `POST /upload-certification/` - Upload a certification file (.docx)
- `GET /delete-certification/<int:cert_id>/` - Delete a specific certification

#### Profile Photo Endpoints
- `POST /upload-profile-photo/<int:employee_id>/` - Upload a new profile photo for an employee
- `POST /delete-photo/<int:employee_id>/` - Delete the current profile photo and reset to default

### Media Access
The application also provides access to uploaded media files through the URL configured in `settings.MEDIA_URL`.

## Contributors
- Komang Wahyu Agastya
- Ni Made Ayu Pranasanthi Dewi

## Contact Information
For further inquiries, please contact:
- [Komang Wahyu Agastya](https://www.linkedin.com/in/wahyuagast)
- [Ni Made Ayu Pranasanthi Dewi](https://www.linkedin.com/in/ayupranasanthi)

## License
MIT License

Copyright (c) 2025 Komang Wahyu Agastya, Ni Made Ayu Pranasanthi Dewi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.