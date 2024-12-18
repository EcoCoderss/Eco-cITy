import json
import csv

def export_to_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
