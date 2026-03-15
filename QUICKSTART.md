# Quick Start Guide

This guide will help you get both the backend and frontend running quickly.

## Prerequisites

- Python 3.11+
- Node.js 16+
- PostgreSQL 12+ (Local) OR Neon DB account (Recommended)

## Backend Setup

1. **Navigate to backend directory**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Database**

**Option A: Neon DB (Recommended - No local setup required)**
1. Sign up at https://neon.tech
2. Create a new project
3. Copy the connection string (looks like: `postgresql://user:pass@ep-xxx.region.aws.neon.tech/dbname`)
4. Use it in your .env file

**Option B: Local PostgreSQL**
```bash
# Create database
createdb taskdb

# Or using psql
psql -U postgres
CREATE DATABASE taskdb;
\q
```

5. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your database credentials and generate a SECRET_KEY
```

**For Neon DB:**
```env
DATABASE_URL=postgresql://user:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=<generate-using-command-below>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**For Local PostgreSQL:**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
SECRET_KEY=<generate-using-command-below>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate SECRET_KEY:
```bash
openssl rand -hex 32
```

6. **Run the backend**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000
API Documentation: http://localhost:8000/docs

## Frontend Setup

1. **Open a new terminal and navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## Using the Application

### 1. Register a New User (Auto-Login)

- Navigate to http://localhost:3000
- Click "Register here"
- Fill in your name, email, and password (min 6 characters)
- Click "Register"
- **You'll be automatically logged in and redirected to the dashboard!**

### 2. Login (If Already Registered)

- Navigate to http://localhost:3000/login
- Enter your email and password
- Click "Login"
- You'll be redirected to the dashboard

### 3. Create Tasks

- On the dashboard, use the "Create New Task" form
- Enter a title and optional description
- Select status (pending/completed)
- Click "Create Task"

### 4. Manage Tasks

- View all your tasks in the task list
- Click "Edit" to modify a task
- Click "Mark as Completed/Pending" to toggle status
- Click "Delete" to remove a task

## Testing the API

You can test the API using the Swagger UI at http://localhost:8000/docs

### Example: Register User (Returns Token)
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

Response:
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "user": {
      "id": "...",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "user"
    },
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer"
  }
}
```

### Example: Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

### Example: Create Task (with token)
```bash
curl -X POST "http://localhost:8000/api/v1/tasks/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "Complete project",
    "description": "Finish the FastAPI backend",
    "status": "pending"
  }'
```

## Docker Setup (Optional)

### Backend with Docker Compose

```bash
cd backend
docker-compose up -d
```

This will start both PostgreSQL and the API.

## Troubleshooting

### Backend Issues

**Database connection error:**
- Verify PostgreSQL is running
- Check DATABASE_URL in .env file
- Ensure database exists

**Import errors:**
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Frontend Issues

**CORS errors:**
- Ensure backend is running on port 8000
- Check CORS configuration in backend/app/main.py

**API connection failed:**
- Verify backend is running
- Check API_BASE_URL in frontend/src/api/axios.js

**Token not persisting:**
- Check browser localStorage
- Clear browser cache and try again

## Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Application entry
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── routers/        # API routes
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utilities
│   ├── requirements.txt
│   └── README.md
│
└── frontend/               # React frontend
    ├── src/
    │   ├── api/           # Axios config
    │   ├── components/    # React components
    │   ├── context/       # Context providers
    │   ├── pages/         # Page components
    │   ├── services/      # API services
    │   └── utils/         # Utilities
    ├── package.json
    └── README.md
```

## Next Steps

- Explore the API documentation at http://localhost:8000/docs
- Read backend/README.md for backend details
- Read frontend/README.md for frontend details
- Customize the application to your needs

## Support

For issues or questions:
- Check the README files in backend/ and frontend/
- Review the API documentation
- Check browser console for frontend errors
- Check terminal logs for backend errors
