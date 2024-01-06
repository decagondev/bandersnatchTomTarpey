class Machine:
    """A customized Random Forest Classifier tailored for working with our dataset.

        Attributes:
        -----------
        name : str
            A descriptor for the classifier, defaulted to "Random Forest Classifier".
        model : RandomForestClassifier
            The trained and tuned Random Forest model.
        timestamp : str
            The date and time when the model was trained.

    """

    def __init__(self, df):
        """
            Initializes the Random Forest Classifier model with the given dataset and fits it to the data.
            Creates timestamp after model has been fit to the data.

            Parameters:
            -----------
            df : pd.DataFrame
                A dataframe where 'Rarity' is the target column and the rest are feature columns.
        """
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(n_estimators=100, n_jobs=-1, max_depth=30, bootstrap=False,
                                            criterion='gini', max_features='log2', min_samples_leaf=1,
                                            min_samples_split=2)
        self.model.fit(features, target)
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __call__(self, feature_basis):
        """
            Predicts the rarity and its probability for the given features.

            Parameters:
            -----------
            feature_basis : pd.DataFrame
                A dataframe containing the features for which predictions need to be made.

            Returns:
            --------
            prediction : str
                The predicted class.
            probability : float
                The probability of the predicted class.
        """
        prediction, *_ = self.model.predict(feature_basis)
        probas, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(probas)

    def save(self, filepath):
        """
            Saves the current instance to the specified filepath.

            Parameters:
            -----------
            filepath : str
                The path where the current instance should be saved.
        """
        dump(self, filepath)

    @staticmethod
    def open(filepath):
        """
            Loads and returns a saved model from the given filepath.

            Parameters:
            -----------
            filepath : str
                The path from which the instance should be loaded.

            Returns:
            --------
                The loaded instance of the class.
        """
        return load(filepath)

    def info(self):
        """
            Provides a string description of the classifier with its timestamp.

            Returns:
            --------
            str
                A string formatted as: "Currently running {name}, from {timestamp}".
        """
        pass
