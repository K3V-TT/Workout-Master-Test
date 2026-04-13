from fastapi import Request
from fastapi.responses import HTMLResponse
from sqlmodel import select
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep
from app.models import Routine
from . import router, templates


@router.get("/app", response_class=HTMLResponse)
async def user_home_view(
    request: Request,
    user: AuthDep,
    db: SessionDep,
):
    routines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()
    return templates.TemplateResponse(
        request=request,
        name="app.html",
        context={
            "user": user,
            "routines": routines,
        },
    )
