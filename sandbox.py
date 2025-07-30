import json
import os
from concurrent.futures import ThreadPoolExecutor

import pythainlp
from module.path import get_all_files, record_path

def process_file(file: str, model: str):
    result_path = record_path(os.path.join("tokenize", model), file, ".json")

    if result_path.exists():
        print(f"✔ Skipping (already converted): {result_path}")
        return

    try:
        with open(file, "r", encoding="utf-8") as f:
            original_text = f.read()

        tokenize_text = pythainlp.word_tokenize(original_text, engine=model)

        result_path.parent.mkdir(parents=True, exist_ok=True)
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump(tokenize_text, f, ensure_ascii=False)

        print(f"✔ Tokenized: {result_path}")
    except Exception as e:
        print(f"✖ Error processing {file}: {e}")

def run_model(model: str):
    files = get_all_files("Source")

    with ThreadPoolExecutor(max_workers=5) as executor:
        for file in files:
            executor.submit(process_file, file, model)

if __name__ == "__main__":
    for model in ["deepcut", "longest", "newmm"]:
        print(f"▶ Tokenizing using model: {model}")
        run_model(model)
