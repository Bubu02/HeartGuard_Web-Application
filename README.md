# HeartGuard: Heart Disease Detection Web Application

HeartGuard is a web application designed to predict whether a person has heart disease based on certain parameters. It uses a machine learning model trained with Scikit-learn, pandas, matplotlib, and numpy libraries.

## Machine Learning Model

The machine learning model was trained and tested using several algorithms including Random Forest, K-Nearest Neighbors (KNN), Support Vector Machines (SVM), and Logistic Regression. After performing hyperparameter tuning, the KNN model was found to be the best model with an accuracy of 99%. The trained model was then saved as a joblib file named "Heart Disease Recognition model_KNeighborClassifier.joblib" for future use.

## Web Application

The web application was built using Flask, a micro web framework written in Python. It takes in user input through a form, processes the data, and uses the trained machine learning model to predict whether the person has heart disease.

## Database

The application uses a SQLite database to store the data. The database model was created using SQLAlchemy, a SQL toolkit and Object-Relational Mapping (ORM) system for Python.

## Usage

To use the application, the user needs to input the required parameters. The application will then predict whether the person has heart disease and display the result.

## Future Work

We plan to continue improving the accuracy of our machine learning model and add more features to the web application. Stay tuned for updates!

## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## License

This project is licensed under the terms of the MIT license.
