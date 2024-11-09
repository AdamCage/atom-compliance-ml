import os
import zipfile
import shutil


def build():
    # with open("../config/config.yaml") as config:
    #     version_app = yaml.safe_load(config)["version_app"]

    source_dir = '../../atom-compliance-ml'
    # output_filename = f'../../atom-compliance-ml-{version_app}-release.zip'
    output_filename = f'../artifacts/atom-compliance-ml-test-release.zip'

    # with zipfile.ZipFile(output_filename, 'w') as zipf:
    #     for root, dirs, files in os.walk(source_dir):
    #         if 'venv' in root:
    #             continue
    #         if '__pycache__' in root:
    #             continue
    #         for file in files:
    #             file_path = os.path.join(root, file)
    #             zipf.write(file_path, os.path.relpath(file_path, source_dir))
    source_dir = os.path.abspath('../../atom-compliance-ml')
    output_dir = os.path.abspath('../artifacts')
    output_filename = os.path.join(output_dir, f'atom-compliance-ml-test-release.zip')

    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            if any(excluded in root for excluded in {'venv', 'node_modules', 'build', '__pycache__', 'dist'}):
                continue

            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, rel_path)
    print("File create success")


if __name__ == '__main__':
    build()
