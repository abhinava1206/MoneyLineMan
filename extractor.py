from datetime import date, timdelta
import pandas as pd
from bs4 import BeautifulSoup

def scan_games(n_days: int) -> pd.DataFrame:
    
