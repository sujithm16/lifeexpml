from lifexp import logger
from lifexp.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from lifexp.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from lifexp.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from lifexp.pipeline.stage4_model_trainer import modelTrainingPipeline
from lifexp.pipeline.stage5_model_evaluation import modelEvaluationPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_val = DataValidationTrainingPipeline()
    data_val.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_trainer = modelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_eval = modelEvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e