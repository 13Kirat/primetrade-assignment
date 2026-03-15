/**
 * Task Service
 * Handles all task-related API calls
 */
import axiosInstance from '../api/axios'

export const taskService = {
  /**
   * Get all tasks
   */
  getTasks: async () => {
    const response = await axiosInstance.get('/tasks/')
    return response.data
  },

  /**
   * Get a specific task by ID
   */
  getTaskById: async (taskId) => {
    const response = await axiosInstance.get(`/tasks/${taskId}`)
    return response.data
  },

  /**
   * Create a new task
   */
  createTask: async (taskData) => {
    const response = await axiosInstance.post('/tasks/', taskData)
    return response.data
  },

  /**
   * Update an existing task
   */
  updateTask: async (taskId, taskData) => {
    const response = await axiosInstance.put(`/tasks/${taskId}`, taskData)
    return response.data
  },

  /**
   * Delete a task
   */
  deleteTask: async (taskId) => {
    const response = await axiosInstance.delete(`/tasks/${taskId}`)
    return response.data
  },
}
