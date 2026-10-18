from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Mo phong chung khoan abc-12")

# Cấu hình đường dẫn tĩnh cho CSS và Video
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cấu hình thư mục chứa giao diện HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"name": "Hồ Hoàng Nhật Khánh"})

@app.get("/health")
async def health():
    return {"status": "ok"}