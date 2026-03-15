# Task Management Full-Stack Application

A production-ready full-stack application with FastAPI backend and React frontend, featuring JWT authentication, role-based access control, and complete CRUD operations for task management.

## 🚀 Features

### Backend (FastAPI)
- **JWT Authentication**: Secure token-based authentication with auto-login on registration
- **Role-Based Access Control**: Admin and User roles
- **Clean Architecture**: Modular structure with separation of concerns
- **PostgreSQL Database**: Robust relational database with SQLAlchemy ORM (Neon DB compatible)
- **Input Validation**: Pydantic schemas for request/response validation
- **Security**: SHA-256 password hashing with salt (no length restrictions), SQL injection protection
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Logging**: Comprehensive logging for debugging and monitoring

### Frontend (React + Vite)
- **Modern React**: Built with React 18 and Vite
- **JWT Authentication**: Secure login and registration with auto-login
- **Protected Routes**: Route guards for authenticated pages
- **Task Management**: Full CRUD operations
- **Context API**: Global state management
- **Axios Interceptors**: Automatic token attachment
- **Error Handling**: Comprehensive error messages
- **Loading States**: User feedback during async operations
- **Seamless Registration**: Users automatically logged in after registration

## 📁 Project Structure

```
.
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── main.py            # Application entry point
│   │   ├── config.py          # Configuration management
│   │   ├── database.py        # Database setup
│   │   ├── models/            # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── user_schema.py
│   │   │   └── task_schema.py
│   │   ├── routers/           # API routes
│   │   │   ├── auth_routes.py
│   │   │   └── task_routes.py
│   │   ├── services/          # Business logic
│   │   │   ├── auth_service.py
│   │   │   └── task_service.py
│   │   ├── dependencies/      # FastAPI dependencies
│   │   │   └── auth_dependency.py
│   │   ├── utils/             # Utility functions
│   │   │   ├── security.py
│   │   │   ├── response.py
│   │   │   └── logger.py
│   │   └── core/              # Core constants
│   │       └── constants.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
│
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── api/               # Axios configuration
│   │   │   └── axios.js
│   │   ├── components/        # React components
│   │   │   ├── Navbar.jsx
│   │   │   ├── TaskForm.jsx
│   │   │   ├── TaskList.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   ├── context/           # Context providers
│   │   │   └── AuthContext.jsx
│   │   ├── hooks/             # Custom hooks
│   │   │   └── useAuth.js
│   │   ├── pages/             # Page components
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── services/          # API services
│   │   │   ├── authService.js
│   │   │   └── taskService.js
│   │   ├── utils/             # Utilities
│   │   │   └── token.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── .env.example
│   └── README.md
│
├── QUICKSTART.md              # Quick start guide
└── README.md                  # This file
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Python 3.11+** - Programming language
- **PostgreSQL** - Relational database (Neon DB compatible)
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **JWT** - Token-based authentication
- **SHA-256** - Password hashing with salt
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client
- **Context API** - State management
- **CSS3** - Styling

## 🚦 Quick Start

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📚 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get JWT token
- `GET /api/v1/auth/me` - Get current user info

### Tasks
- `GET /api/v1/tasks/` - Get all tasks
- `POST /api/v1/tasks/` - Create new task
- `GET /api/v1/tasks/{id}` - Get specific task
- `PUT /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

## 🔐 Authentication Flow

**Registration (Auto-Login):**
1. User registers with name, email, and password
2. Backend creates account and returns JWT token
3. Frontend stores token and sets user in context
4. User is automatically logged in and redirected to dashboard

**Login:**
1. User enters credentials
2. Backend validates and returns JWT token
3. Frontend stores token and fetches user data
4. User is redirected to dashboard

**Token Management:**
- Token automatically attached to all API requests via Axios interceptor
- Backend validates token on protected routes
- 401 responses trigger automatic logout and redirect

## 👥 Role-Based Access

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

## 🐳 Docker Support

### Backend with Docker Compose
```bash
cd backend
docker-compose up -d
```

This starts both PostgreSQL and the API.

## 📖 Documentation

- **Backend API Docs**: http://localhost:8000/docs (Swagger UI)
- **Backend ReDoc**: http://localhost:8000/redoc
- **Backend README**: [backend/README.md](backend/README.md)
- **Frontend README**: [frontend/README.md](frontend/README.md)

## 🧪 Testing

### Backend
```bash
cd backend
pytest  # When tests are implemented
```

### Frontend
```bash
cd frontend
npm test  # When tests are implemented
```

## 🔧 Configuration

### Backend Environment Variables

**Neon DB (Recommended):**
```env
DATABASE_URL=postgresql://user:password@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Local PostgreSQL:**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend Environment Variables
```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

## 🚀 Production Deployment

### Backend
1. Set `DEBUG=False` in .env
2. Use strong SECRET_KEY
3. Configure CORS properly
4. Use HTTPS
5. Set up database backups
6. Use production ASGI server (Gunicorn + Uvicorn)

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Frontend
```bash
npm run build
# Deploy dist/ folder to your hosting service
```

## 🔍 Key Features Explained

### Backend
- **Clean Architecture**: Separation of concerns with models, schemas, services, and routes
- **Dependency Injection**: FastAPI's dependency system for auth and database sessions
- **ORM**: SQLAlchemy for type-safe database operations
- **Validation**: Pydantic schemas ensure data integrity
- **Security**: SHA-256 password hashing with salt, JWT tokens, SQL injection protection
- **Auto-Login**: Registration returns JWT token for immediate authentication
- **Neon DB Support**: Fully compatible with Neon serverless PostgreSQL

### Frontend
- **Component-Based**: Reusable React components
- **Context API**: Global auth state management
- **Protected Routes**: Automatic redirect for unauthenticated users
- **Axios Interceptors**: Automatic token attachment and error handling
- **Form Validation**: Client-side validation with error messages
- **Auto-Login on Registration**: Seamless UX without manual login step

## 📈 Scalability Considerations

### Current Architecture
- Modular design for easy feature addition
- Service layer for business logic separation
- Dependency injection for testability

### Future Enhancements
1. **Redis Caching** - Cache frequently accessed data
2. **Docker Containerization** - Full containerization
3. **Horizontal Scaling** - Load balancer with multiple instances
4. **Microservices** - Separate auth and task services
5. **Database Optimization** - Read replicas, connection pooling
6. **Monitoring** - Prometheus, Grafana, ELK stack

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Ensure all dependencies are installed

**Frontend can't connect to backend:**
- Verify backend is running on port 8000
- Check CORS configuration
- Verify API_BASE_URL in axios.js

**Authentication not working:**
- Check JWT token in localStorage
- Verify SECRET_KEY matches between requests
- Check token expiration time

## 📝 License

MIT License

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📧 Support

For issues or questions:
- Check the documentation
- Review the API docs at http://localhost:8000/docs
- Check browser console for frontend errors
- Check terminal logs for backend errors

## 🎯 Next Steps

1. Explore the API documentation
2. Customize the UI styling
3. Add more features (tags, priorities, due dates)
4. Implement unit and integration tests
5. Set up CI/CD pipeline
6. Deploy to production

---

Built with ❤️ using FastAPI and React
