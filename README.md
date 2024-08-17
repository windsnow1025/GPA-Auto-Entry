# WES iGPA Calculator Automation

This project automates the process of entering course data into the WES iGPA Calculator using Selenium. It reads course information from an Excel file and populates the calculator fields, saving you time and effort.

## Features

* **Automated Data Entry:** Reads course data (title, credit, grade) from an Excel file.
* **Selenium Integration:** Uses Selenium to interact with the WES iGPA Calculator website.
* **Error Handling:** Includes basic error handling for file reading and data validation.

## Requirements

* Python 3
* Libraries:
    * selenium
    * pandas

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your data:**
   * Create an Excel file (e.g., `sign_score.xlsx`) with the following columns:
     * `title`: Course title
     * `credit`: Course credits
     * `grade`: Course grade (using the WES iGPA grading scale)
2. **Update the file path:**
   * In `main.py`, modify the `excel_file` variable to point to your Excel file:
     ```python
     excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path
     ```
3. **Run the script:**
   ```bash
   python main.py
   ```

## How it Works

1. The script reads course data from the specified Excel file using the `read_excel_data` function.
2. It initializes a Selenium WebDriver (using Chrome by default).
3. It creates an instance of the `WESiGPA` class, which handles interaction with the WES iGPA Calculator website.
4. The `add_courses_from_data` method iterates through the course data and populates the calculator fields for each course.
5. The script waits for manual setup (up to 2 minutes) to allow you to select the country and education system on the WES iGPA Calculator page.
6. After the data is entered, the browser remains open so you can review the results.
7. Press Enter to close the browser.

## Files

* **`scraper.py`:** Contains the base `Scraper` class for web scraping tasks.
* **`wes_igpa.py`:** Contains the `WESiGPA` class, which extends the `Scraper` class and handles interaction with the WES iGPA Calculator.
* **`excel_reader.py`:** Contains the `read_excel_data` function for reading data from an Excel file.
* **`main.py`:** The main script that orchestrates the process.
* **`requirements.txt`:** Lists the required Python libraries.

## Example Data (sign_score.xlsx)

| title         | credit | grade |
|---------------|--------|-------|
| Math 101      | 3      | 88    |
| Physics 101   | 4      | 92    |
| Chemistry 101 | 3      | 95    |
| ...           | ...    | ...   |

## Note

* The script waits for up to 2 minutes to allow you to manually select the country and education system on the WES iGPA Calculator page. You can adjust this timeout if needed.
