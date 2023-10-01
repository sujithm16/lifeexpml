import os
from lifexp import logger
from lifexp.utils.common import get_size
from lifexp.entity import DataTransformationConfig
from lifexp import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def eda(self):
        data = pd.read_csv(self.config.data_path)

        data['Country'] = le.fit_transform(data['Country'])
        data['Status'] = le.fit_transform(data['Status'])
        logger.info(data['Status'])
        logger.info(data['Country'])
        
        data.rename(columns={'Life expectancy ':'Life_expectancy',"Adult Mortality": 'Adult_Mortality',
                            'infant deaths': 'infant_deaths','percentage expenditure': 'percentage_expenditure',
                            'Hepatitis B': 'Hepatitis_B','Measles ': 'Measles','BMI ': 'BMI',
                            'under-five deaths ': 'under_five_deaths','Total expenditure': 'Total_expenditure',
                            'Diphtheria  ': 'Diphtheria','HIV/AIDS': 'HIV_AIDS',
                            'thinness  1-19 years': 'thinness_1_19_years',
                            'thinness 5-9 years': 'thinness_5_9_years',
                            'Income composition of resources': 'Income_composition_of_resources'},inplace=True)
        
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        