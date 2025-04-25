from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import database
from fastapi.responses import HTMLResponse

# import file html in path templates
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

#html
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI with HTML</title>
        </head>
        <body>
            <h1>Welcome to FastAPI!</h1>
            <p>This is a simple HTML response.</p>
        </body>
    </html>
    """

# نموذج البيانات
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# === التعديل هنا ===
if __name__ == "__main__":
    # استبدل "main" باسم ملف البايثون الخاص بك (بدون .py) إذا كان مختلفاً
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
    # لاحظ: تم إزالة workers=1 لأن reload يعمل فقط مع worker واحد.