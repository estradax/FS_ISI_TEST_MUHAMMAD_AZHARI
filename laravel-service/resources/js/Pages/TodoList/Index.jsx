import React, { useState } from 'react'
import { router } from '@inertiajs/react'

import TodoForm from './components/TodoForm'
import TodoItem from './components/TodoItem'

export default function Index(props) {
  const [selectedTodo, setSelectedTodo] = useState(null)
  const [isError, setIsError] = useState(false)

  function onSuccess() {
    router.reload()
  }

  function onEditClick(todo) {
    setSelectedTodo(todo)
  }

  function onError() {
    setIsError(true)
  }

  return (
    <div className="mx-auto max-w-[580px] mt-8">
      <h1 className="text-center text-4xl">Task Management</h1>
      {props.error ? (
        <p className="mt-4 text-center">
          Something went wrong, try again later
        </p>
      ) : (
        <>
          <TodoForm todo={selectedTodo} onSuccess={onSuccess} />
          {isError ? (
            <div className="bg-red-500 text-white rounded-lg p-2 mt-4">
              <p className="text-center">
                Something went wrong, try again later.
              </p>
            </div>
          ) : null}
          <div className="mt-6">
            <h2 className="font-bold mb-4">Ongoing Task</h2>
            <div className="grid gap-2">
              {props.ongoing_todos.map((todo) => (
                <TodoItem
                  key={todo.id}
                  todo={todo}
                  onUpdateSuccess={onSuccess}
                  onDeleteSuccess={onSuccess}
                  onEditClick={onEditClick}
                  onError={onError}
                />
              ))}
            </div>
          </div>
          <div className="mt-4">
            <h2 className="font-bold mb-4">Completed Task</h2>
            <div className="grid gap-2">
              {props.completed_todos.map((todo) => (
                <TodoItem
                  key={todo.id}
                  todo={todo}
                  onUpdateSuccess={onSuccess}
                  onDeleteSuccess={onSuccess}
                  onEditClick={onEditClick}
                  onError={onError}
                />
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  )
}
