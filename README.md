# Who Are You Most Like?

**Who Are You Most Like?** is a personality-matching application that identifies the most similar characters to a user based on their behavioral traits. The app compares user responses to a dataset of over 1000 characters, including cartoon characters and public figures.

## Project Description

This project combines data science and personality profiling to provide a fun yet structured tool for personality analysis. Users answer a series of five multiple-choice questions. Each question corresponds to one behavioral dimension. The responses are transformed into a numerical personality vector, which is then compared against a dataset using cosine similarity.

The app returns the top character matches in two categories:

* Cartoon characters
* Modern public figures

## Features

* Interactive personality quiz
* Trait-based matching using cosine similarity
* Two application formats:

  * Jupyter Notebook version (for direct exploration of code)
  * Streamlit web application (for end-user interaction)
* Clear matching results by category

## Dataset

The dataset includes more than 1000 characters with pre-assigned values for five behavioral traits:

* BAP1: Intelligence / Analytical thinking
* BAP2: Calmness / Emotional control
* BAP3: Irritability / Reactivity
* BAP4: Courage / Assertiveness
* BAP5: Cheerfulness / Sociability

Each character is also labeled with a category (`Cartoon` or `Modern`).

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Regular Expressions

## How to Run

### Option 1: Using Streamlit App

1. Make sure you have Streamlit installed:

   ```
   pip install streamlit
   ```

2. Run the app:

   ```
   streamlit run who_are_you_streamlit.py
   ```

3. The quiz will launch in your browser.

### Option 2: Using Jupyter Notebook

1. Open the notebook version in any Jupyter environment.
2. Run all cells to load the dataset and interact with the quiz through the console.

## Folder Structure

* `unique_1000_characters_dataset.csv` - Main dataset with character traits
* `who_are_you_streamlit.py` - Streamlit version of the app
* `who_are_you_notebook.ipynb` - Jupyter version of the app

## Future Work

* Add 10,000+ character profiles
* Include historical and fictional categories
* Introduce sentiment-based open-text input
* Add charts and visual insights

## License

This project is for educational and demonstration purposes. Dataset is custom-built and intended for non-commercial use.
