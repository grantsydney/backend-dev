from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True

class TaskBase(BaseModel):
    name: str
    description: str | None = None
    tag: str
    created_time: str
    updated_time: str
    task_id: str

class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    # items: list[Item] = []
    tasks: list[Task] = []

    class Config:
        orm_mode = True
