# Building Currency Converter in Python

## Author
Name: Watcharapong Narod 
Student ID: 25020076

## Description
This application provides a user-friendly interface to convert currencies using the Frankfurt API.

Challenges faced:
- Handling API rate limits and ensuring consistent data retrieval.
- Ensuring accurate currency conversions, especially with historical data.

Future Features:
- Adding a graphical representation of currency trends over time.
- Implementing caching to improve response times for frequently requested currency pairs.

## How to Setup
1. Ensure you have Python installed. This project uses Python version 3.11.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Install the required packages using pip: pip install -r requirements.txt
(Note: Ensure you have a `requirements.txt` file with all the necessary packages and their versions.)

## How to Run the Program
1. Navigate to the project directory in your terminal or command prompt.
2. Run the following command to start the Streamlit app: streamlit run app.py
3. Open the provided link in your web browser to access the currency converter application.

## Project Structure
- `app.py`: Main Streamlit application script, handles UI and user interactions.
- `api.py`: Contains general functions for making API calls.
- `frankfurter.py`: Functions specific to the Frankfurt API.
- `currency.py`: Functions for formatting and displaying conversion results.
- `README.md`: Documentation and details about the project.

## Citations
- Frankfurt API for currency conversion: [Frankfurt API Documentation](https://www.frankfurter.app/docs/)

