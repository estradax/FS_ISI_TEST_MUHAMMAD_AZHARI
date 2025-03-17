import React from 'react'
import { Pencil, X, Check } from 'lucide-react'

export default function TodoItem(props) {
  return (
    <div className="flex justify-between items-center bg-[#D0D0D0] rounded-lg p-4">
      <div>
        <div className="flex items-center gap-2">
          <p className={`${props.todo.isCompleted ? 'line-through' : null}`}>
            Update task form
          </p>
          <Pencil size="18" />
        </div>
        <p className="text-sm mt-2">25 Mar 2023 19:00</p>
      </div>
      <div className="flex gap-2">
        <div className="flex items-center justify-center border-2 rounded-full w-[25px] h-[25px]">
          <X size="20" strokeWidth={2.5} />
        </div>
        <div
          className={`flex items-center justify-center border-2 rounded-full ${props.todo.isCompleted ? null : 'bg-white'} w-[25px] h-[25px]`}
        >
          {props.todo.isCompleted ? (
            <Check size="18" strokeWidth={2.5} />
          ) : null}
        </div>
      </div>
    </div>
  )
}
