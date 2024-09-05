# WES iGPA Calculator Automation

This project automates the process of entering course data into the GPA Calculator using Selenium. It reads course information from an Excel file and populates the calculator fields, saving you time and effort.

## Features

- **Automated Data Entry:** Reads course data (title, credit, grade) from an Excel file.
- **Selenium Integration:** Uses Selenium to interact with the WES iGPA Calculator website and Scholaro GPA Calculator.
- **Error Handling:** Includes basic error handling for file reading and data validation.

## Requirements

- Python 3
- Libraries:
  - selenium
  - pandas

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

## Example Data (sign_score.xlsx)

| title         | credit | grade |
|---------------|--------|-------|
| Math 101      | 3      | 88    |
| Physics 101   | 4      | 92    |
| Chemistry 101 | 3      | 95    |
| ...           | ...    | ...   |

## Note

* The script waits for up to 2 minutes to allow you to manually enter information on the webpage. You can adjust this timeout if needed.
