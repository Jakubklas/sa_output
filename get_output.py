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
    

    def get_sa_outputs(self, waveplan:pd.DataFrame, col_map:dict= COL_MAP, nd_only:bool=True):
        if nd_only:
            waveplan = waveplan[waveplan["Cycle"].isin(['CYCLE_1', 'CYCLE_2'])]

        # Get common Date/Station/Cycle/Wave identifier
        waveplan["Key"] = waveplan["Key"] + waveplan["Wave Number"].astype(str)

        # Iterate throught the df & copy the number of rows * Blocks per wave
        sa = []
        counter = 0
        for idx, row in waveplan.iterrows():
            
            for _ in range(row["Blocks"]+1):  # Inclusive range
                sa.append(row)
            
            counter +=1
            if counter % 50 == 0:
                print(f"Rows processed {counter}")

        sa = pd.DataFrame(sa)
        sa.rename(columns=col_map, inplace=True)
        sa = sa[COL_MAP.values()]
     
        return sa


    def remove_accepted_offers(self):
        pass



if __name__ == "__main__":
    sa = SaOutput(next_week=False)
    print("Reading wave plan...\n")
    waveplan = sa.read_waveplan()
    print("Wave Plan read...\n")
    print("Creating SA offers...\n")
    sa_out = sa.get_sa_outputs(waveplan, COL_MAP, nd_only=True)
    print(sa_out.head(40))