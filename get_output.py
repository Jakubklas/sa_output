import pandas as pd
from datetime import datetime, timedelta

from config import * 

class SaOutput:
    def __init__(self, wave_plan_path:str= WAVEPLAN_PATH, next_week:bool =True) -> None:
        self.wave_plan_path = wave_plan_path
        add_wk = (1 if next_week else 0)
        self.year = (datetime.now() + timedelta(weeks=(add_wk or 0))).year
        self.week = (datetime.now() + timedelta(weeks=(add_wk or 0))).isocalendar().week

    
    def read_waveplan(self) -> pd.DataFrame:
        print(str(self.year) + "-" + str(self.week))
        df = pd.read_excel(self.wave_plan_path, engine="openpyxl", sheet_name="Data")
        mask = df["YearWeek"] == str(self.year) + "-" + str(self.week)
        df = df[mask]
        
        return df
    

if __name__ == "__main__":
    sa = SaOutput(next_week=False)
    print(sa.read_waveplan().head())