import os

LINE = "Our newest topping: lukewarm mayonnaise, applied by a chef who winked and whispered 'trust me' — the pizza has since filed for divorce."

# Ensure the output directory exists (it does in the grading container).
os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(LINE)
