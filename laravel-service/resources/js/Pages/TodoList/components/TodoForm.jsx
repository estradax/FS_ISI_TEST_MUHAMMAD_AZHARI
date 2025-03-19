import React, { useState, useEffect } from 'react'

export default function TodoForm(props) {
  const [title, setTitle] = useState('')
  const [error, setError] = useState(null)
  const [isEditing, setIsEditing] = useState(false)

  useEffect(() => {
    if (props.todo) {
      setTitle(props.todo.title)
      setIsEditing(true)
    }
  }, [props.todo])

  async function onSubmit() {
    setError(null)
    try {
      await axios.post('/api/v1/todos', { title })
      setTitle('')
      props.onSuccess()
    } catch (e) {
      if (e.status === 422) {
        setError('Title is required')
      }
    }
  }

  async function onSubmitUpdate() {
    setError(null)
    try {
      await axios.put(`/api/v1/todos/${props.todo.id}`, {
        title,
        is_completed: props.todo.is_completed,
      })
      setTitle('')
      setIsEditing(false)
      props.onSuccess()
    } catch (e) {
      if (e.status === 422) {
        setError('Title is required')
      }
    }
  }

  function onCancel() {
    setTitle('')
    setIsEditing(false)
  }

  return (
    <>
      <div className="flex flex-col">
        <label>Title</label>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="border-[0.5px] border-black rounded-xl py-2 px-4"
          type="text"
        />
        {error ? <p className="text-sm text-red-600">{error}</p> : null}
      </div>
      <div className="flex justify-center mt-8 gap-2">
        {!isEditing ? (
          <button
            onClick={onSubmit}
            className="bg-[#6FCBFF] px-4 py-1 rounded-md"
            type="button"
          >
            Add Task
          </button>
        ) : (
          <>
            <button
              onClick={onSubmitUpdate}
              className="bg-[#FFB46F] px-4 py-1 rounded-md"
              type="button"
            >
              Update Task
            </button>
            <button
              onClick={onCancel}
              className="bg-[#FF6F6F] px-4 py-1 rounded-md"
              type="button"
            >
              Cancel
            </button>
          </>
        )}
      </div>
    </>
  )
}
