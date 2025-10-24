import sys 
import pandas as pd 
from src.exception import CustomException
from src.utils import load_model_object


class PredictPipeline:
    def __init(self):
        pass

    def predict(self,data_frame):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_model_object(file_path=model_path)
            preprocessor = load_model_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(data_frame)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
                 Sex:str,
                 ChestPainType:str,
                 RestingECG:str,
                 ExerciseAngina:str,
                 ST_Slope:str,
                 Age:int,
                 Cholesterol:int,
                 FastingBS:int,
                 MaxHR:int,
                 Oldpeak:int,
                 RestingBP:int):
        
        self.Sex =Sex
        
        self.ChestPainType = ChestPainType

        self.RestingECG = RestingECG

        self.ExerciseAngina = ExerciseAngina

        self.ST_Slope = ST_Slope

        self.Age = Age

        self.Cholesterol = Cholesterol

        self.FastingBS = FastingBS

        self.MaxHR = MaxHR

        self.Oldpeak = Oldpeak

        self.RestingBP = RestingBP
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
            "Sex": [self.Sex],
            "ChestPainType": [self.ChestPainType],
            "RestingECG": [self.RestingECG],
            "ExerciseAngina": [self.ExerciseAngina],
            "ST_Slope": [self.ST_Slope],
            "Age": [self.Age],
            "Cholesterol": [self.Cholesterol],
            "FastingBS": [self.FastingBS],
            "MaxHR": [self.MaxHR],
            "Oldpeak": [self.Oldpeak],
            "RestingBP": [self.RestingBP]
        }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)