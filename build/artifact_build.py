import yaml
import shutil


def build():
    version_app = yaml.safe_load("version_app")
    source_dir = '../../atom-compliance-ml'
    output_filename = f'artifacts/atom-compliance-ml-{version_app}-release'
    shutil.make_archive(output_filename, 'zip', source_dir)


if __name__ == '__main__':
    build()
