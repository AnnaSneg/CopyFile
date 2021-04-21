import os
from xml.etree import ElementTree
import shutil


def parse_config(config_file_name: str):
    all_tree = ElementTree.parse(config_file_name).getroot()
    lst_path = []
    for tag in all_tree.findall('file'):
        source_path = tag.get('source_path')
        destination_path = tag.get('destination_path')
        file_name = tag.get('file_name')
        tpl = (source_path, destination_path, file_name)
        lst_path.append(tpl)
    return lst_path


def copy_files(files_to_copy):
    for part in files_to_copy:
        source_path, destination_path, file_name = part[0], part[1], part[2]
        print("Copy", os.path.join(source_path, file_name), "to", destination_path)
        try:
            shutil.copy(os.path.join(source_path, file_name), destination_path)
            print("One file copied")
        except:
            print("Copy failed")


if __name__ == "__main__":
    files_to_copy = parse_config('config.xml')
    copy_files(files_to_copy)

