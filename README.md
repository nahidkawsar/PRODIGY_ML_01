# PRODIGY_ML_01
# House Price Prediction
![front page](https://github.com/user-attachments/assets/3309c1b6-4249-400a-a0b7-13575b0dfdc7)

This repository contains a machine learning model for predicting house prices based on various features. The project includes a Flask web application to provide an interface for users to input data and get predictions.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Creating the Model](#creating-the-model)
- [Running the Flask App](#running-the-flask-app)
- [Using the Web Application](#using-the-web-application)

## Project Structure

├── app.py

├── house_price_1.pkl

├── static
│ └── house.jpg

├── templates
│ └── index.html


![stracture](https://github.com/user-attachments/assets/f1530ac7-3705-4c86-b72d-daa42f2f9c92)



- `app.py`: The Flask web application.
- `house_price_1.pkl`: The pre-trained machine learning model.
- `static/house.jpg`: Background image for the web app.
- `templates/index.html`: HTML file for the web interface.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Anaconda (recommended for managing dependencies)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nahidkawsar/PRODIGY_ML_01.git
cd PRODIGY_ML_01
```

2. Create a virtual environment and activate it:
```bash
conda create -n house_price_prediction python=3.8
conda activate house_price_prediction
```


3. Install the required packages:

```bash
pip install flask numpy pickle5
```

## Creating the Model
If you need to create the model from scratch, follow these steps:

- Open the My task 1.ipynb Jupyter notebook and execute all cells to train and save the model as house_price_1.pkl.
- Ensure the house_price_1.pkl file is placed in the root directory of this project.
## Running the Flask App:

1. Navigate to the project directory:

```bash
cd /d path\to\house-price-prediction
```

2. Run the Flask application:

```bash
python app.py
```

```bash
The app will start running on http://.......
```


## Using the Web Application
1. Open your web browser and go to http://..........
2. Enter the required details in the form:

- Name
- LotFrontage
- LotArea
- GrLivArea
- BsmtFullBath
- BsmtHalfBath
- FullBath
- HalfBath
- BedroomAbvGr
- KitchenAbvGr
3. Click the "Predict" button to see the predicted house price.
