import pickle
import numpy as np

class ModelWrapper:
    def __init__(self, model_path: str = "./models/best_model.pkl"):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        self.country_features = {
            "India": {"gdp_per_capita": 2000, "health_spending": 3.5, "education_index": 0.6},
            "USA": {"gdp_per_capita": 60000, "health_spending": 16.9, "education_index": 0.9}
        }

    def _features_to_array(self, features: dict) -> list:
        return [features.get("gdp_per_capita", 0), features.get("health_spending", 0), features.get("education_index", 0)]

    def predict_single(self, features: dict) -> float:
        arr = np.array(self._features_to_array(features)).reshape(1, -1)
        return float(self.model.predict(arr)[0])

    def predict_country(self, country: str) -> float:
        features = self.country_features.get(country)
        if not features:
            raise ValueError("Unknown country")
        return self.predict_single(features)

    def predict_all(self) -> dict:
        return {c: self.predict_single(f) for c, f in self.country_features.items()}