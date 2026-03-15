/**
 * Task List Component
 * Displays list of tasks with actions
 */
import { useState } from 'react'
import TaskForm from './TaskForm'

const TaskList = ({ tasks, onUpdate, onDelete }) => {
  const [editingTask, setEditingTask] = useState(null)

  const handleEdit = (task) => {
    setEditingTask(task)
  }

  const handleCancelEdit = () => {
    setEditingTask(null)
  }

  const handleUpdate = async (taskData) => {
    await onUpdate(editingTask.id, taskData)
    setEditingTask(null)
  }

  const handleToggleStatus = async (task) => {
    const newStatus = task.status === 'pending' ? 'completed' : 'pending'
    await onUpdate(task.id, { status: newStatus })
  }

  if (tasks.length === 0) {
    return <div className="empty-state">No tasks yet. Create your first task!</div>
  }

  return (
    <div className="task-list">
      {tasks.map((task) => (
        <div key={task.id} className="task-card">
          {editingTask?.id === task.id ? (
            <TaskForm
              initialData={editingTask}
              onSubmit={handleUpdate}
              onCancel={handleCancelEdit}
            />
          ) : (
            <>
              <div className="task-header">
                <h3 className="task-title">{task.title}</h3>
                <span className={`task-status status-${task.status}`}>
                  {task.status}
                </span>
              </div>
              
              {task.description && (
                <p className="task-description">{task.description}</p>
              )}
              
              <div className="task-meta">
                <small>Created: {new Date(task.created_at).toLocaleDateString()}</small>
              </div>

              <div className="task-actions">
                <button
                  onClick={() => handleToggleStatus(task)}
                  className="btn btn-small btn-toggle"
                >
                  Mark as {task.status === 'pending' ? 'Completed' : 'Pending'}
                </button>
                <button
                  onClick={() => handleEdit(task)}
                  className="btn btn-small btn-edit"
                >
                  Edit
                </button>
                <button
                  onClick={() => onDelete(task.id)}
                  className="btn btn-small btn-delete"
                >
                  Delete
                </button>
              </div>
            </>
          )}
        </div>
      ))}
    </div>
  )
}

export default TaskList
