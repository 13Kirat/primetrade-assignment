/**
 * Axios Configuration
 * Centralized HTTP client with interceptors
 */
import axios from 'axios'
import { getToken, removeToken } from '../utils/token'

// Use environment variable or fallback to Railway URL
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://primetrade-assignment-production.up.railway.app/api/v1'

// Create axios instance
const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  // Note: withCredentials set to false to avoid CORS preflight issues
  withCredentials: false,
})

// Request interceptor - attach JWT token
axiosInstance.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor - handle 401 errors
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      removeToken()
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default axiosInstance
