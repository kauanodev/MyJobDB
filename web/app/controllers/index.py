from fastapi import Request, Response
from datetime import datetime

from app.settings import TEMPLATES


class IndexController():

    def index(self, request: Request, response: Response):
        user_agent = request.headers.get("User-Agent")
        response.headers.append("Content-Type", "text/html")
        utc_now = datetime.utcnow()
        return TEMPLATES.TemplateResponse(
            "index.html",
            {"request": request, "user_agent": user_agent,
                "utc_now": utc_now, "items": [1, 2, 3, 1]}
        )
