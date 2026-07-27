from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
import traceback

from backend.predict import predict_image
from backend.llm_report import generate_report

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Advanced AI Medical Intelligence Platform API Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = predict_image(file_path)

        report = generate_report(
            result["prediction"],
            result["confidence"]
        )

        result["report"] = report
        result["heatmap"] = None

        return result

    except Exception as e:

        traceback.print_exc()

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(e)
            }
        )