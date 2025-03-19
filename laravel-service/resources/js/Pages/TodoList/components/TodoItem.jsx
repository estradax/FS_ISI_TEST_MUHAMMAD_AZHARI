import React from 'react'
import moment from 'moment'
import { Pencil, X, Check } from 'lucide-react'

export default function TodoItem(props) {
  async function onCheckClick() {
    try {
      const isCompleted = !props.todo.is_completed
      await axios.put(`/api/v1/todos/${props.todo.id}`, {
        title: props.todo.title,
        is_completed: isCompleted,
      })
      props.onUpdateSuccess()
    } catch (e) {
      props.onError()
    }
  }

  function onPencilClick() {
    props.onEditClick(props.todo)
  }

  async function onDeleteClick() {
    try {
      await axios.delete(`/api/v1/todos/${props.todo.id}`)
      props.onDeleteSuccess()
    } catch (e) {
      props.onError()
    }
  }

  return (
    <div className="flex justify-between items-center bg-[#D0D0D0] rounded-lg p-4">
      <div>
        <div className="flex items-center gap-2">
          <p className={`${props.todo.is_completed ? 'line-through' : null}`}>
            {props.todo.title}
          </p>
          <Pencil onClick={onPencilClick} size="18" />
        </div>
        <p className="text-sm mt-2">
          {moment(props.todo.created_at).format('DD MMM YYYY HH:mm')}
        </p>
      </div>
      <div className="flex gap-2">
        <div
          onClick={onDeleteClick}
          className="flex items-center justify-center border-2 rounded-full w-[25px] h-[25px]"
        >
          <X size="20" strokeWidth={2.5} />
        </div>
        <div
          onClick={onCheckClick}
          className={`flex items-center justify-center border-2 rounded-full ${props.todo.is_completed ? null : 'bg-white'} w-[25px] h-[25px]`}
        >
          {props.todo.is_completed ? (
            <Check size="18" strokeWidth={2.5} />
          ) : null}
        </div>
      </div>
    </div>
  )
}
