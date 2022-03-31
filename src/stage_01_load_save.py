from src.utils.all_utils import read_yaml, create_dir
import argparse
import os
import pandas as pd
import shutil
from tqdm import tqdm

def copy_file(source_download_path, local_data_dir):
    list_of_file = os.listdir(source_download_path)
    N = len(list_of_file)
    for file in tqdm(list_of_file,total=N,desc= f"copying fiel from {source_download_path} to {local_data_dir}",colour="green"):
        src = os.path.join(source_download_path, file)
        dest = os.path.join(local_data_dir, file)
        shutil.copy(src, dest)

def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config['source_download_dirs']
    local_data_dir = config['local_data_path']

    for source_download_path,local_data_dir in tqdm(zip(source_download_dirs,local_data_dir),total=2,desc= "list of folders",colour="red"):
        create_dir([local_data_dir])
        copy_file(source_download_path, local_data_dir)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', "-c", default='config/config.yaml')

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)