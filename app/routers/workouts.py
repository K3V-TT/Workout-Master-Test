from fastapi import Request
from fastapi.responses import HTMLResponse
from sqlmodel import select
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep
from app.models import Routine, Workout
from . import router, templates


@router.get("/workouts", response_class=HTMLResponse)
async def workouts_view(request: Request, user: AuthDep, db: SessionDep):
    workouts = db.exec(select(Workout)).all()
    routines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()
    return templates.TemplateResponse(
        request=request,
        name="workouts.html",
        context={
            "user": user,
            "workouts": workouts,
            "routines": routines,
        },
    )
