# Song Recommender System

**Created by Caleb in September 2022. Uploaded to GitHub in July 2025.**

---

## Overview

The Song Recommender System is a Python-based project that analyzes a dataset of songs and recommends similar tracks based on their features. It leverages data science and machine learning tools (NumPy, pandas, TensorFlow, Numba, etc.) to compute song similarities and generate recommendations. The project also includes scripts for processing word lists and definitions, which can be used for advanced filtering or educational features.

---

## Main Features

- **Song Similarity Calculation:**  
  The core notebooks (`Song Recommender System.ipynb` and `Song Recommender System 2!!.ipynb`) load a dataset (`data.csv`), filter songs by year, and compute a distance matrix between songs using their features. The system then finds and displays the most similar songs for each track.

- **Efficient Computation:**  
  Uses Numba’s JIT compilation (with CUDA support) to accelerate the calculation of pairwise song distances.

- **Data Preparation Utilities:**  
  Includes scripts (`dictionary_creator.py`, `dictmaka.py`, `list_of_words.py`) for generating and formatting word lists and definitions, which are stored in files like `final_words_array.txt` and `word_definitions.txt`.

- **Extensive Vocabulary and Definitions:**  
  The project contains large word lists and detailed definitions, which can be used for educational or filtering purposes.

---

## Project Structure

- **Jupyter Notebooks:**  
  - `Song Recommender System.ipynb`  
  - `Song Recommender System 2!!.ipynb`  
  Main logic for loading data, computing similarities, and displaying recommendations.

- **Data Files:**  
  - `data.csv`: Main dataset of songs and their features.  
  - `final_words_array.txt`, `words.txt`, `more words.txt`, etc.: Word lists for vocabulary features.  
  - `word_definitions.txt`: Definitions for vocabulary words.

- **Utility Scripts:**  
  - `dictionary_creator.py`, `dictmaka.py`, `list_of_words.py`: Scripts for generating and formatting word lists and definitions.

---

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/song-recommender.git
   cd song-recommender
   ```

2. **Install Dependencies:**
   - Make sure you have Python 3.7+ installed.
   - Install required packages (NumPy, pandas, TensorFlow, Numba, ipywidgets, tabulate, etc.):
     ```bash
     pip install numpy pandas tensorflow numba ipywidgets tabulate
     ```

3. **Run the Notebooks:**
   - Open `Song Recommender System.ipynb` or `Song Recommender System 2!!.ipynb` in Jupyter Notebook or JupyterLab.
   - Run all cells to load the data, compute the similarity matrix, and view song recommendations.

4. **(Optional) Generate/Update Word Lists:**
   - Use the utility scripts to process or update word lists and definitions as needed.
   - Example:
     ```bash
     python list_of_words.py
     python dictionary_creator.py
     ```

---

## Notes

- The project was originally created in September 2022, but is being uploaded to GitHub in July 2025.
- The code is designed for educational and experimental purposes. For large datasets, computations may take significant time and memory.
- You can extend the system by adding new features, improving the recommendation logic, or integrating with music APIs.

---

## License

This project is open source and available under the MIT License. 