from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import ModelWrapper
from app.logger import get_logger
from app.monitoring import monitor

logger = get_logger(__name__)
app = FastAPI(title="Life Expectancy Predictor")

model = ModelWrapper(model_path="./models/best_model.pkl")

class PredictRequest(BaseModel):
    country: str | None = None
    features: dict | None = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
@monitor
async def predict(req: PredictRequest):
    try:
        if req.country and req.features:
            pred = model.predict_single(req.features)
            logger.info(f"Prediction for {req.country}: {pred}")
            return {"country": req.country, "prediction": pred}
        elif req.country and not req.features:
            pred = model.predict_country(req.country)
            return {"country": req.country, "prediction": pred}
        else:
            preds = model.predict_all()
            return {"predictions": preds}
    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=str(e))