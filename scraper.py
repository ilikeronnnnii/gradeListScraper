import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# URL of the grade list
url = "https://academic.utm.my/UGStudent/asp/GradeList.asp?kp={INSERT YOUR KP HERE}&ss=202320242&oo=pel"

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to fetch and display the grade list
def fetch_and_display_grades():
    # Make a GET request to fetch the raw HTML content
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the HTML content
    table = soup.find('table', {'border': '1'})

    # Extract table rows
    rows = table.find_all('tr')

    # Extract course names and grades
    data = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        course_name = cells[2].text.strip()
        grade = cells[3].text.strip()
        data.append([course_name, grade])

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=['Course Name', 'Grade'])

    # Clear the console
    clear_console()

    # Display the DataFrame
    print(df)

# Continuously fetch and display grades every 1200 seconds
while True:
    fetch_and_display_grades()
    time.sleep(1200)
