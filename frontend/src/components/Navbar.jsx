/**
 * Navbar Component
 * Navigation bar with user info and logout
 */
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'

const Navbar = () => {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-brand">
          <h2>Task Manager</h2>
        </div>
        <div className="navbar-menu">
          <span className="user-email">{user?.email}</span>
          <button onClick={handleLogout} className="btn btn-logout">
            Logout
          </button>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
