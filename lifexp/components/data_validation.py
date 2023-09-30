import pandas as pd
from lifexp.config.configuration import DataValidationConfig
import os
from pathlib import Path
from lifexp import logger

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config
            
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
        
    def missing_values(self):
        data = pd.read_csv(self.config.unzip_data_dir)
        data.dropna(inplace=True)
        data.to_csv(os.path.join(self.config.root_dir, "Life Expectancy Data cleaned.csv"),index = False)
        logger.info(data.shape)

        
            
            