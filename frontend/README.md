# Task Management Frontend

A production-ready React frontend application built with Vite that integrates with the FastAPI backend for task management with JWT authentication.

## Features

- **JWT Authentication**: Secure login and registration with auto-login
- **Protected Routes**: Route guards for authenticated pages
- **Task Management**: Full CRUD operations for tasks
- **Role-Based Access**: Support for user and admin roles
- **Responsive Design**: Clean and simple UI
- **Error Handling**: Comprehensive error messages
- **Loading States**: User feedback during async operations
- **Token Management**: Automatic token attachment and storage
- **Seamless Registration**: Users are automatically logged in after registration

## Tech Stack

- **React 18** - UI library
- **Vite** - Build tool and dev server
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client
- **Context API** - State management
- **CSS3** - Styling

## Project Structure

```
frontend/
├── src/
│   ├── api/
│   │   └── axios.js              # Axios configuration
│   ├── components/
│   │   ├── Navbar.jsx            # Navigation bar
│   │   ├── TaskForm.jsx          # Task creation/edit form
│   │   ├── TaskList.jsx          # Task list display
│   │   └── ProtectedRoute.jsx   # Route protection
│   ├── context/
│   │   └── AuthContext.jsx       # Authentication context
│   ├── hooks/
│   │   └── useAuth.js            # Auth hook
│   ├── pages/
│   │   ├── Login.jsx             # Login page
│   │   ├── Register.jsx          # Registration page
│   │   └── Dashboard.jsx         # Main dashboard
│   ├── services/
│   │   ├── authService.js        # Auth API calls
│   │   └── taskService.js        # Task API calls
│   ├── utils/
│   │   └── token.js              # Token utilities
│   ├── App.jsx                   # Main app component
│   ├── main.jsx                  # Entry point
│   └── index.css                 # Global styles
├── index.html
├── package.json
├── vite.config.js
└── README.md
```

## Installation

### Prerequisites

- Node.js 16+ and npm
- Backend API running on `http://localhost:8000`

### Setup Steps

1. **Navigate to frontend directory**
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

The application will be available at `http://localhost:3000`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## API Integration

The frontend connects to the FastAPI backend at `http://localhost:8000/api/v1`

### Authentication Endpoints

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user info

### Task Endpoints

- `GET /tasks/` - Get all tasks
- `POST /tasks/` - Create new task
- `GET /tasks/{id}` - Get specific task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

## Features Explained

### Authentication Flow

1. User registers or logs in
2. JWT token is stored in localStorage
3. Token is automatically attached to all API requests
4. User data is fetched and stored in context
5. Protected routes check for valid token

### Token Management

- Tokens are stored in localStorage
- Axios interceptor automatically attaches token to requests
- 401 responses trigger automatic logout and redirect

### Protected Routes

Routes wrapped in `<ProtectedRoute>` component:
- Check for valid token
- Redirect to login if not authenticated
- Show loading state during verification

### Task Management

- Create tasks with title, description, and status
- View all tasks (users see only their tasks)
- Edit tasks inline
- Toggle task status (pending/completed)
- Delete tasks with confirmation

### Error Handling

- Form validation errors
- API error messages
- Network error handling
- 401 unauthorized handling

## Usage

### Register New User

1. Navigate to `/register`
2. Fill in name, email, and password (min 6 characters)
3. Submit form
4. Account is created and you're automatically logged in
5. Redirected to dashboard immediately (no need to login separately)

### Login

1. Navigate to `/login`
2. Enter email and password
3. Submit form
4. Redirected to dashboard

### Manage Tasks

1. View all tasks on dashboard
2. Create new task using form
3. Edit task by clicking "Edit" button
4. Toggle status with "Mark as" button
5. Delete task with "Delete" button

## Configuration

### API Base URL

Update in `src/api/axios.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

### Vite Proxy

Configured in `vite.config.js` for development:
```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8000',
    changeOrigin: true,
  }
}
```

## Production Build

1. **Build the application**
```bash
npm run build
```

2. **Preview production build**
```bash
npm run preview
```

3. **Deploy dist folder** to your hosting service

## Environment Variables

Create `.env` file for environment-specific configuration:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

Update `src/api/axios.js`:
```javascript
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### CORS Issues

Ensure backend has CORS middleware configured:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Token Not Persisting

Check browser localStorage:
```javascript
localStorage.getItem('access_token')
```

### API Connection Failed

Verify backend is running on `http://localhost:8000`

## Future Enhancements

- TypeScript migration
- Unit and integration tests
- State management with Redux/Zustand
- Real-time updates with WebSockets
- Advanced filtering and sorting
- Pagination for large datasets
- Dark mode support
- Internationalization (i18n)

## License

MIT License
