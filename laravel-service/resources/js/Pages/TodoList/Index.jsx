import React from 'react'

import TodoItem from './components/TodoItem'

export default function Index(props) {
  return (
    <div className="mx-auto max-w-[580px] mt-8">
      <h1 className="text-center text-4xl">Task Management</h1>
      <div className="flex flex-col">
        <label>Title</label>
        <input
          className="border-[0.5px] border-black rounded-xl py-2 px-4"
          type="text"
        />
      </div>
      <div className="flex justify-center mt-8">
        <button className="bg-[#6FCBFF] px-4 py-1 rounded-md" type="button">
          Add Task
        </button>
      </div>
      <div className="mt-6">
        <h2 className="font-bold mb-4">Ongoing Task</h2>
        <TodoItem todo={{ isCompleted: false }} />
      </div>
      <div className="mt-4">
        <h2 className="font-bold mb-4">Completed Task</h2>
        <TodoItem todo={{ isCompleted: true }} />
      </div>
    </div>
  )
}
