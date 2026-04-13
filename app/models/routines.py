from typing import Optional
from sqlmodel import Field, SQLModel


class RoutineBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None, nullable=True)
    user_id: int = Field(index=True)


class Routine(RoutineBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class RoutineWorkoutBase(SQLModel):
    routine_id: int = Field(foreign_key="routine.id")
    workout_id: int = Field(foreign_key="workout.id")
    order: int = Field(default=0)


class RoutineWorkout(RoutineWorkoutBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
