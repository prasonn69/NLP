# Spam Email Classifier

A machine learning-powered email classifier that determines whether a message is spam or ham (legitimate email) using Natural Language Processing techniques.

## Features

- **Text Classification**: Uses TF-IDF vectorization and Naive Bayes algorithm
- **Interactive Web Interface**: Built with Streamlit for easy testing
- **Real-time Predictions**: Instant classification of email messages
- **User-friendly Interface**: Simple text input with clear results

## Technologies Used

- **Python 3.x**
- **Scikit-learn**: Machine learning library for model training
- **Pandas**: Data manipulation and analysis
- **Streamlit**: Web application framework
- **Joblib**: Model serialization

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd spam-email-classifier
```

2. Install required dependencies:
```bash
pip install pandas scikit-learn streamlit joblib
```

3. Download the spam dataset and place it in the appropriate directory:
   - Dataset should be named `spam.csv`
   - Place it in `/Users/prason/Downloads/` or update the path in the code

## Usage

### Training the Model

The model training is included in the main script. When you run the application for the first time, it will:

1. Load and preprocess the spam dataset
2. Split data into training and testing sets
3. Create a pipeline with TF-IDF vectorizer and Multinomial Naive Bayes classifier
4. Train the model and save it as `model.pkl`

### Running the Web Application

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter an email message in the text area

4. Click "Classify" to get the prediction

## Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Pipeline**: Combines preprocessing and classification in a single workflow
- **Output**: Binary classification (Spam or Ham)

## Dataset

The model expects a CSV file with the following structure:
- `v1`: Labels (ham/spam)
- `v2`: Email messages

## File Structure

```
spam-email-classifier/
├── app.py              # Main application file
├── model.pkl           # Trained model (generated after first run)
├── spam.csv           # Dataset file
└── README.md          # This file
```

## Example Usage

Input: "Congratulations! You've won $1000! Click here to claim your prize!"
Output: **Spam**

Input: "Hey, are we still meeting for lunch tomorrow?"
Output: **Ham**

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- Add model performance metrics display
- Include confidence scores for predictions
- Support for bulk email classification
- Integration with email APIs
- Advanced preprocessing techniques
- Model comparison with other algorithms
