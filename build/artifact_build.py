import yaml
import os
import zipfile


def build():
    # with open("../config/config.yaml") as config:
    #     version_app = yaml.safe_load(config)["version_app"]

    source_dir = '../../atom-compliance-ml'
    # output_filename = f'../../atom-compliance-ml-{version_app}-release.zip'
    output_filename = f'../../atom-compliance-ml-test-release.zip'

    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Пропускаем каталог `venv`
            if 'venv' in root:
                continue
            if '__pycache__' in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))


if __name__ == '__main__':
    build()