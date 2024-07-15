from flask import Flask, request, render_template  # Import necessary Flask modules for web development
import pickle  # Import pickle for loading the pre-trained model
import numpy as np  # Import numpy for handling array operations

app = Flask(__name__, static_url_path='/static')  # Initialize the Flask application and set static URL path

model = pickle.load(open('house_price_1.pkl', 'rb'))  # Load the pre-trained regression model

@app.route('/')  # Define the home route
def home():  # Function to handle requests to the home route
    return render_template('index.html')  # Render the index.html template for the home page

@app.route('/predict', methods=['POST'])  # Define the predict route to handle POST requests
def predict():  # Function to handle requests to the predict route
    if request.method == 'POST':  # Check if the request method is POST
        # Retrieve data from the form submitted by the user
        LotFrontage = float(request.form['LotFrontage'])  # Get the 'LotFrontage' field and convert to float
        LotArea = float(request.form['LotArea'])        # Get the 'LotArea' field and convert to integer
        GrLivArea = float(request.form['GrLivArea'])      # Get the 'GrLivArea' field and convert to integer
        BsmtFullBath = int(request.form['BsmtFullBath'])  # Get the 'BsmtFullBath' field and convert to integer
        BsmtHalfBath = int(request.form['BsmtHalfBath'])  # Get the 'BsmtHalfBath' field and convert to integer
        FullBath = int(request.form['FullBath'])  # Get the 'FullBath' field and convert to integer
        HalfBath = int(request.form['HalfBath'])  # Get the 'HalfBath' field and convert to integer
        BedroomAbvGr = int(request.form['BedroomAbvGr'])  # Get the 'BedroomAbvGr' field and convert to integer
        KitchenAbvGr = float(request.form['KitchenAbvGr'])  # Get the 'KitchenAbvGr' field and convert to integer

        # Make prediction using the loaded regression model
        prediction = model.predict([[LotFrontage, LotArea, GrLivArea, BsmtFullBath, BsmtHalfBath, FullBath, HalfBath, BedroomAbvGr, KitchenAbvGr]])

        predicted_price = float(prediction[0])  # Convert the predicted price to a scalar value

        # Prepare output message
        output_message = f"Predicted House Price: ${predicted_price:,.2f}"  # Format predicted price as a dollar amount

        # Render the index.html template with the prediction result displayed
        return render_template('index.html', results=output_message)
        
    else:  # If the request method is not POST (e.g., GET request)
        # Render the index.html template for user interaction (initial page load)
        return render_template('index.html')

if __name__ == "__main__":  # Check if the script is run directly by the Python interpreter
    # Run the Flask application on host 0.0.0.0 (accessible from all network interfaces),
    # port 5000, with debug mode enabled for development purposes
    app.run(host='0.0.0.0', port=5000, debug=True)
