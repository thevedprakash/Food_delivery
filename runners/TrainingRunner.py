import os
import sys
sys.path.append('src')
import json
import logging
from model import model_list
from load_data import load_data
from prepare_data import prepare_data
from preprocessing import convert_categorical_columns
from train import model_training

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TrainingRunner(object):
    """
    This runner is to run the training pipeline.
    """
    def __init__ (self,config):
        self.train = config["train_path"]
        self.na_values = config["na_values"]
        self.model_dir = config["model_dir"]
        self.encoded_filename = config["encoded_filename"]
        self.model_list = model_list
        self.target_column = config["target_column"]  

    def run(self):
        logger.info(f"Starting the training pipeline.")
        df = load_data(self.train, self.na_values)
        prepare_data(df)
        convert_categorical_columns(df,self.target_column,self.model_dir,self.encoded_filename)
        model_training(df,self.target_column,self.model_list,self.model_dir)
            
if __name__ == "__main__":

    config_file = "config.json"

    if os.path.isfile(config_file):
        with open(config_file, 'rb') as f:
            config = json.load(f)

    runner = TrainingRunner(config)
    runner.run()