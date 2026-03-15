# Task Management API

A production-ready FastAPI backend with JWT authentication, role-based access control (RBAC), and clean architecture.

## Features

- **JWT Authentication**: Secure token-based authentication with auto-login on registration
- **Role-Based Access Control**: Admin and User roles with different permissions
- **Clean Architecture**: Modular structure with separation of concerns
- **PostgreSQL Database**: Robust relational database with SQLAlchemy ORM (Neon DB compatible)
- **Input Validation**: Pydantic schemas for request/response validation
- **Security**: SHA-256 password hashing with salt, SQL injection protection
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Logging**: Comprehensive logging for debugging and monitoring
- **Scalable Design**: Ready for horizontal scaling and microservices

## Tech Stack

- **FastAPI** - Modern Python web framework
- **Python 3.11+** - Programming language
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **JWT** - Token-based authentication
- **SHA-256** - Password hashing with salt
- **Uvicorn** - ASGI server

## Project Structure

```
backend/
├── app/
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── user_schema.py
│   │   └── task_schema.py
│   ├── routers/             # API routes
│   │   ├── auth_routes.py
│   │   └── task_routes.py
│   ├── services/            # Business logic
│   │   ├── auth_service.py
│   │   └── task_service.py
│   ├── dependencies/        # FastAPI dependencies
│   │   └── auth_dependency.py
│   ├── utils/               # Utility functions
│   │   ├── security.py
│   │   ├── response.py
│   │   └── logger.py
│   └── core/                # Core constants
│       └── constants.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
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

4. **Setup PostgreSQL database**

**Option A: Local PostgreSQL**
```bash
# Create database
createdb taskdb

# Or using psql
psql -U postgres
CREATE DATABASE taskdb;
```

**Option B: Neon DB (Recommended)**
1. Sign up at [neon.tech](https://neon.tech)
2. Create a new project
3. Copy the connection string
4. Use it in your .env file

5. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

**For Local PostgreSQL:**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
```

**For Neon DB:**
```env
DATABASE_URL=postgresql://user:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
```

Generate a secure SECRET_KEY:
```bash
openssl rand -hex 32
```

6. **Run the application**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/login` | Login and get JWT token | No |
| GET | `/api/v1/auth/me` | Get current user info | Yes |

### Tasks

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/tasks/` | Create new task | Yes |
| GET | `/api/v1/tasks/` | Get all tasks | Yes |
| GET | `/api/v1/tasks/{task_id}` | Get specific task | Yes |
| PUT | `/api/v1/tasks/{task_id}` | Update task | Yes |
| DELETE | `/api/v1/tasks/{task_id}` | Delete task | Yes |

## Usage Examples

### Register User (Auto-Login)
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

Response includes JWT token for immediate login:
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "user": {...},
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer"
  }
}
```

### Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

### Create Task
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

## Database Schema

### Users Table
- `id` (UUID) - Primary key
- `name` (String) - User's full name
- `email` (String) - Unique email address
- `password_hash` (String) - Hashed password
- `role` (String) - User role (admin/user)
- `is_active` (Boolean) - Account status
- `created_at` (DateTime) - Registration timestamp

### Tasks Table
- `id` (UUID) - Primary key
- `title` (String) - Task title
- `description` (String) - Task description
- `status` (String) - Task status (pending/completed)
- `owner_id` (UUID) - Foreign key to users
- `created_at` (DateTime) - Creation timestamp
- `updated_at` (DateTime) - Last update timestamp

## Role-Based Access Control

### User Role
- Create tasks
- View own tasks only
- Update own tasks only
- Delete own tasks only

### Admin Role
- View all users
- View all tasks
- Delete any task
- Full system access

## Security Features

- **Password Hashing**: SHA-256 with random 32-byte salt (no length restrictions)
- **JWT Tokens**: Secure token-based authentication
- **Token Expiry**: 30-minute token lifetime (configurable)
- **Auto-Login on Registration**: Seamless user experience with immediate token generation
- **SQL Injection Protection**: SQLAlchemy ORM parameterized queries
- **Input Validation**: Pydantic schema validation
- **Environment Variables**: Sensitive data in .env file
- **Neon DB Compatible**: Works seamlessly with Neon serverless PostgreSQL

## Scalability Considerations

### Current Architecture
- Modular design for easy feature addition
- Service layer for business logic separation
- Dependency injection for testability

### Future Enhancements

1. **Redis Caching**
   - Cache frequently accessed data
   - Session management
   - Rate limiting

2. **Docker Containerization**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
   ```

3. **Horizontal Scaling**
   - Load balancer (Nginx/HAProxy)
   - Multiple API instances
   - Shared PostgreSQL database
   - Redis for session sharing

4. **Microservices Migration**
   - Separate auth service
   - Separate task service
   - API Gateway
   - Message queue (RabbitMQ/Kafka)

5. **Database Optimization**
   - Read replicas
   - Connection pooling
   - Query optimization
   - Database indexing

6. **Monitoring & Observability**
   - Prometheus metrics
   - Grafana dashboards
   - ELK stack for logs
   - Sentry for error tracking

## Testing

Run tests (when implemented):
```bash
pytest
```

## Production Deployment

1. Set `DEBUG=False` in .env
2. Use strong SECRET_KEY
3. Configure CORS properly
4. Use HTTPS
5. Set up database backups
6. Implement rate limiting
7. Use production ASGI server (Gunicorn + Uvicorn)

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request
