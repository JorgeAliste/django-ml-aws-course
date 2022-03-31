import pickle


def make_titanic_prediction(pclass, sex, age, sibsp, parch, fare, embarked):
    x = [[pclass, sex, age, sibsp, parch, fare, embarked]]
    rf_clf = pickle.load(open('ml_aws_course/ml_models/random_forest_model.sav', 'rb'))
    prediction = rf_clf.predict(x)
    return prediction
