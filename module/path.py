from pathlib import Path

def get_all_files(directory: str):
    base_path = Path(directory)
    return [
        str(file)
        for file in base_path.rglob('*')
        if file.is_file() and not file.name.startswith('.') # ignore a file start with dot(.)
    ]
    
def record_path(result_root: str, source_path: str, type:str) -> Path:
    source_path = Path(source_path)
    relative_path = source_path.relative_to(source_path.parts[0])
    new_path = Path(result_root) / relative_path
    new_path = new_path.with_suffix(type)
    new_path.parent.mkdir(parents=True, exist_ok=True)
    return new_path