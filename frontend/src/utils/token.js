/**
 * Token Management Utilities
 * Handles JWT token storage in localStorage
 */

const TOKEN_KEY = 'access_token'

/**
 * Store JWT token in localStorage
 */
export const setToken = (token) => {
  localStorage.setItem(TOKEN_KEY, token)
}

/**
 * Retrieve JWT token from localStorage
 */
export const getToken = () => {
  return localStorage.getItem(TOKEN_KEY)
}

/**
 * Remove JWT token from localStorage
 */
export const removeToken = () => {
  localStorage.removeItem(TOKEN_KEY)
}

/**
 * Check if user is authenticated
 */
export const isAuthenticated = () => {
  return !!getToken()
}
