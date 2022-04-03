from typing import List

class LeakDetection:
    """
    For correct automatic evaluation please implement your prediction logic inside this class
    """

    def __init__(self, dirname='.'):
        self.model = self.load_model(dirname)

    def load_model(self, dirname):
        """
        Loads your pretrained model to use it for prediction.
        Please use os.path.join(location_to_dir, model_file_name)

        :param dirname: Path to directory where model is located
        :return: your pretrained model, if no model is required return None

        Example:
            import os
            import joblib
            load(os.path.join(self.dirname, 'tree.joblib'))

        """
        return None

    def predict(self, features: List) -> bool:
        """
        Your implementation for prediction. If leak is detected it should return true.

        :param features: A list of features
        :return: should return true if leak is detected. Otherwise, it should return false.

        Example:
            return self.model.predict(features) == 0

        """
        return True
