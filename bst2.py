import pandas as pd
import json

with open('points.json', 'r', encoding='utf-8') as f:
    points_data = json.load(f)

points_series = pd.Series(points_data)

distances = points_series.diff().dropna().abs()

distances.to_json('len.json', orient='index', indent=4, force_ascii=False)

print("Відстані між сусідніми точками збережені у файл len.json")
