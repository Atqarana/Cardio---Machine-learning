
# Heart Disease Prediction and Monitoring API

## Overview

The **Heart Disease Prediction and Monitoring API** is a robust backend service built using FastAPI. This API leverages various machine learning algorithms to predict the likelihood of heart disease in patients. After testing multiple algorithms, we optimized our model using Random Forest to achieve the highest accuracy, further refining it for enhanced performance.

## Features

- **Multiple Machine Learning Algorithms**: 
  - Linear Regression
  - Logistic Regression
  - Decision Tree
  - Support Vector Machine (SVM)
  - Naive Bayes
  - Random Forest
  - K-Nearest Neighbors (KNN)
  - Neural Networks

- **High Accuracy**: The final model employs Random Forest, refined to maximize predictive accuracy of 97%.

- **Easy Integration**: Designed for seamless integration into applications for heart disease prediction.

## Technologies Used

- **Backend Framework**: FastAPI
- **Machine Learning Libraries**: 
  - Scikit-learn
  - Pandas
  - NumPy
  - TensorFlow/Keras (for Neural Networks)
  - Matplotlib/Seaborn (for visualization)
- **Data Handling**: Pandas and NumPy for data manipulation

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd heart-disease-prediction-api
2. **Install Dependencies**:

```bash

pip install -r requirements.txt
```
3. **Run the API **:

```bash

uvicorn main:app --reload
```
## Usage
The API exposes endpoints to input patient data and receive heart disease predictions.

Example Request
```bash

POST /predict
Content-Type: application/json

{
  "age": 54,
  "sex": 1,
  "cp": 2,
  "trestbps": 140,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.5,
  "slope": 2,
  "ca": 0,
  "thal": 2,
  "target": 1
}
```
Example Response

``` json
Copy code
{
  "prediction": 1,
  "probability": 0.85
}
```
## Project Highlights
This project exemplifies the ability to integrate machine learning with modern web technologies, providing an accessible solution for heart disease prediction. The use of FastAPI ensures high performance and scalability, making it suitable for real-time applications.

## Contributing
We welcome contributions! To contribute:

**Fork the repository**.
- Create a new branch (git checkout -b feature/YourFeature).
- Make your changes and commit them (git commit -m 'Add your feature').
- Push to the branch (git push origin feature/YourFeature).
- Open a pull request.
- 
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
