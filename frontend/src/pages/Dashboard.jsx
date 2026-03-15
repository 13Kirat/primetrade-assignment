/**
 * Dashboard Page
 * Main application page with task management
 */
import { useState, useEffect } from 'react'
import Navbar from '../components/Navbar'
import TaskForm from '../components/TaskForm'
import TaskList from '../components/TaskList'
import { taskService } from '../services/taskService'

const Dashboard = () => {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [successMessage, setSuccessMessage] = useState('')

  // Fetch tasks on mount
  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    try {
      setLoading(true)
      const response = await taskService.getTasks()
      setTasks(response.data.tasks)
      setError('')
    } catch (err) {
      setError('Failed to load tasks')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleCreateTask = async (taskData) => {
    try {
      await taskService.createTask(taskData)
      showSuccess('Task created successfully')
      fetchTasks()
    } catch (err) {
      throw err
    }
  }

  const handleUpdateTask = async (taskId, taskData) => {
    try {
      await taskService.updateTask(taskId, taskData)
      showSuccess('Task updated successfully')
      fetchTasks()
    } catch (err) {
      setError('Failed to update task')
      console.error(err)
    }
  }

  const handleDeleteTask = async (taskId) => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return
    }

    try {
      await taskService.deleteTask(taskId)
      showSuccess('Task deleted successfully')
      fetchTasks()
    } catch (err) {
      setError('Failed to delete task')
      console.error(err)
    }
  }

  const showSuccess = (message) => {
    setSuccessMessage(message)
    setTimeout(() => setSuccessMessage(''), 3000)
  }

  return (
    <div className="dashboard">
      <Navbar />
      
      <div className="dashboard-container">
        <div className="dashboard-header">
          <h1>My Tasks</h1>
        </div>

        {error && <div className="error-message">{error}</div>}
        {successMessage && <div className="success-message">{successMessage}</div>}

        <div className="dashboard-content">
          <div className="task-form-section">
            <TaskForm onSubmit={handleCreateTask} />
          </div>

          <div className="task-list-section">
            <h2>All Tasks ({tasks.length})</h2>
            {loading ? (
              <div className="loading-container">
                <div className="spinner"></div>
                <p>Loading tasks...</p>
              </div>
            ) : (
              <TaskList
                tasks={tasks}
                onUpdate={handleUpdateTask}
                onDelete={handleDeleteTask}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
