import csv
from pathlib import Path


scores_for_csv = [

    ["name","score"],
    ["LLCoolDave",	23],
    ["LLCoolDave",	27],
    ["red",	12],
    ["LLCoolDave",	26],
    ["tom123",	26],
    ["O_O",	7],
    ["Misha46",	24],
    ["O_O",	14],
    ["Empiro",	18],
    ["Empiro",	18],
    ["MaxxT",	25],
    ["L33tH4x",	42],
    ["Misha46",	25],
    ["johnsmith",	30],
    ["Empiro",	23],
    ["O_O",	22],
    ["MaxxT",	25],
    ["Misha46",	24],

]

scores_csv_path = Path.home() / "scores.csv"
with scores_csv_path.open(mode= "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(scores_for_csv)
file.close()


with scores_csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    scores = [row for row in reader]
file.close()

high_scores = {}
for item in scores:
    name = item["name"]
    score = int(item["score"])
    # If the name has not been added to the high_score dictionary, then
    # create a new key with the name and set its value to the score
    if name not in high_scores:
        high_scores[name] = score
    # Otherwise, check to see if score is greater than the score currently
    # assigned to high_scores[name] and replace it if it is
    else:
        if score > high_scores[name]:
            high_scores[name] = score


output_csv_file = Path.home() / "high_scores.csv"
with output_csv_file.open(mode="w",newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "high_score"])
    writer.writeheader()
    for name in high_scores:
        row_dict = {"name": name, "high_score": high_scores[name]}
        writer.writerow(row_dict)

file.close()



scores_csv_path.unlink()
output_csv_file.unlink()