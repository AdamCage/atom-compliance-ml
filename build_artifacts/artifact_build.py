import os
import zipfile


def build():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.abspath(os.path.join(script_dir, '..'))
    output_dir = os.path.join(source_dir, 'build_artifacts', 'artifacts')
    os.makedirs(output_dir, exist_ok=True)
    output_filename = 'atom-compliance-ml.zip'
    output_path = os.path.join(output_dir, output_filename)
    exclude_dirs = {'venv', '__pycache__', '.git'}
    exclude_files = set()

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files = [f for f in files if f not in exclude_files]
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    print("Архив успешно создан и сохранен в:", output_path)


if __name__ == '__main__':
    build()
