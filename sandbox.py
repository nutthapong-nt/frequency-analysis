import json
import os
import pythainlp
from module.path import get_all_files, record_path

# a model of word tokenize
for file in get_all_files("Source"):

    for model in ["deepcut", "longest", "newmm"]:

        result_path = record_path(os.path.join("tokenize", model), file, ".json")
        if result_path.exists():
            print(f"✔ Skipping (already converted): {result_path}")
            continue

        with open(file, "r", encoding="utf-8") as f:
            original_text = f.read()

        tokenize_text = pythainlp.word_tokenize(original_text, engine="longest")

        with open(
            encoding="utf-8",
        ) as f:
            json.dump(tokenize_text, f, ensure_ascii=False)

    exit()
