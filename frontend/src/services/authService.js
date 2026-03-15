/**
 * Authentication Service
 * Handles all auth-related API calls
 */
import axiosInstance from '../api/axios'

export const authService = {
  /**
   * Register a new user and automatically log them in
   */
  register: async (name, email, password) => {
    const response = await axiosInstance.post('/auth/register', {
      name,
      email,
      password,
    })
    return response.data
  },

  /**
   * Login user and get JWT token
   */
  login: async (email, password) => {
    const response = await axiosInstance.post('/auth/login', {
      email,
      password,
    })
    return response.data
  },

  /**
   * Get current authenticated user
   */
  getCurrentUser: async () => {
    const response = await axiosInstance.get('/auth/me')
    return response.data
  },
}
