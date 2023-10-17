import os
import sys
sys.path.append('src')
import pickle
import joblib
import json
import logging
from load_data import load_data
from prepare_data import prepare_data
from predict import preprocess_and_predict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class InferenceRunner(object):
    """
    This runner is to run the training pipeline.
    """
    def __init__ (self,config):
        self.test = config["test_path"]
        self.test_input = config["test_input"]
        self.na_values = config["na_values"]
        self.model_dir = config["model_dir"]
        self.encoded_filename = config["encoded_filename"]
        self.model_name = config["model_name"]
        self.target_column = config["target_column"]  

        # load encoded dictionary
        self.encoded_filename = os.path.join(self.model_dir,self.encoded_filename)
        with open(self.encoded_filename, 'rb') as handle:
            self.encoded_dict = pickle.load(handle)

        # load saved model
        self.saved_model= joblib.load(os.path.join(self.model_dir,self.model_name))

    def run(self):
        logger.info(f"Starting the Inference pipeline.")
        df = load_data(self.test_input, self.na_values)
        print(df)
        print(df.info())
        logger.info(f"Preparing the data for Inference")
        data = preprocess_and_predict(df,self.encoded_dict)
        logger.info(f"Generating the Inference ")
        print(self.saved_model.predict(data.iloc[0:5,:]))
            
if __name__ == "__main__":

    config_file = "config.json"

    if os.path.isfile(config_file):
        with open(config_file, 'rb') as f:
            config = json.load(f)

    runner = InferenceRunner(config)
    runner.run()