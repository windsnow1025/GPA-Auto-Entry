from selenium import webdriver
from src.wes_igpa import WESiGPA
from excel_reader import read_excel_data

# Load the Excel file
excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path

try:
    # Read data from the Excel file
    course_data = read_excel_data(excel_file)

    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH

    # Create an instance of WESiGPAScraper
    wes_scraper = WESiGPA(driver)

    # Add courses from the Excel data
    wes_scraper.add_courses_from_data(course_data)

    # Keep the browser open for you to see the result
    input("Press Enter to close the browser...")

    # Close the browser after you press Enter
    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")