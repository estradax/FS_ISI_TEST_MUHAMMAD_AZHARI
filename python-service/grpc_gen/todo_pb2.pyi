from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ordering(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASC: _ClassVar[Ordering]
    DESC: _ClassVar[Ordering]
ASC: Ordering
DESC: Ordering

class TodoMessage(_message.Message):
    __slots__ = ("id", "title", "is_completed", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    is_completed: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., is_completed: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetTodosRequest(_message.Message):
    __slots__ = ("is_completed", "ordering")
    IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    is_completed: bool
    ordering: Ordering
    def __init__(self, is_completed: bool = ..., ordering: _Optional[_Union[Ordering, str]] = ...) -> None: ...

class GetTodosResponse(_message.Message):
    __slots__ = ("todos",)
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[TodoMessage]
    def __init__(self, todos: _Optional[_Iterable[_Union[TodoMessage, _Mapping]]] = ...) -> None: ...

class CreateTodoRequest(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class CreateTodoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateTodoRequest(_message.Message):
    __slots__ = ("id", "title", "is_completed")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    is_completed: bool
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., is_completed: bool = ...) -> None: ...

class UpdateTodoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteTodoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
