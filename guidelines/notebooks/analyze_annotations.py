import json
import pandas as pd

def parse_label_studio_json(json_path):
    """
    Parses exported Label Studio JSON data to extract label distribution metrics.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    extracted_records = []

    for task in data:
        task_id = task.get('id')
        for ann in task.get('annotations', []):
            for res in ann.get('result', []):
                value = res.get('value', {})
                # Extract label classifications across text and vision formats
                labels = (
                    value.get('labels') or 
                    value.get('choices') or 
                    value.get('polygonlabels') or 
                    value.get('rectanglelabels')
                )
                if labels:
                    for l in labels:
                        extracted_records.append({'Task_ID': task_id, 'Label': l})

    df = pd.DataFrame(extracted_records)
    print("=== LABEL STUDIO ANNOTATION SUMMARY ===")
    print(f"Total Annotations Analyzed: {len(df)}")
    print("\nClass Counts:")
    print(df['Label'].value_counts())
    return df

if __name__ == "__main__":
    # Analyzes actual JSON export files from workspace
    try:
        df_vision = parse_label_studio_json('project-3-at-2026-08-19-13-37-e584e6aa.json')
    except FileNotFoundError:
        print("Run script directly in directory containing exported JSON files.")
