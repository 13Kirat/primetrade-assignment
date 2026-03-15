/**
 * Authentication Context
 * Manages global auth state and provides auth functions
 */
import { createContext, useState, useEffect } from 'react'
import { authService } from '../services/authService'
import { setToken, getToken, removeToken } from '../utils/token'

export const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  // Load user on mount if token exists
  useEffect(() => {
    const loadUser = async () => {
      const token = getToken()
      if (token) {
        try {
          const response = await authService.getCurrentUser()
          setUser(response.data.user)
        } catch (error) {
          console.error('Failed to load user:', error)
          removeToken()
        }
      }
      setLoading(false)
    }

    loadUser()
  }, [])

  /**
   * Register a new user and automatically log them in
   */
  const register = async (name, email, password) => {
    const response = await authService.register(name, email, password)
    
    // If registration includes token, auto-login the user
    if (response.data.access_token) {
      const token = response.data.access_token
      setToken(token)
      setUser(response.data.user)
    }
    
    return response
  }

  /**
   * Login user
   */
  const login = async (email, password) => {
    const response = await authService.login(email, password)
    const token = response.data.access_token
    setToken(token)
    
    // Fetch user data after login
    const userResponse = await authService.getCurrentUser()
    setUser(userResponse.data.user)
    
    return response
  }

  /**
   * Logout user
   */
  const logout = () => {
    removeToken()
    setUser(null)
  }

  const value = {
    user,
    loading,
    register,
    login,
    logout,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}
