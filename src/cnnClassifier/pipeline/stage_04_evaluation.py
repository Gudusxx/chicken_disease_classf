from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation



STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>.. stage {STAGE_NAME} started <<<<<<<<")
        evaluation = EvaluationPipeline()
        evaluation.main()
        logger.info(f">>>>>>>>.. stage {STAGE_NAME} completed!.. <<<<<<<<\n\nX====================X")
    except Exception as e:
        logger.exception(e)
        raise e


