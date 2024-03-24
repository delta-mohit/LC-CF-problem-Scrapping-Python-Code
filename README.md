# LC/CF Problem Scrapping Python Code
# Web Scraping for Competitive Programming Problems

This Python script allows you to scrape problem details from LeetCode and Codeforces websites and save them to text files.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install Selenium: pip install selenium
3. Download Chrome WebDriver from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the specified location (`C:\\Users\\mohit\\Desktop\\WEB_SCRAPPING\\chromedriver.exe`). Change this path of file according to your system.

## Usage

1. Run the script: python problem.py
2. Enter the problem link when prompted.
3. The script will scrape the problem details and save them to respective text files (`leetcode_problem.txt` for LeetCode and `codeforces_problem.txt` for Codeforces).

## Notes

- Make sure to have an active internet connection.
- The script uses XPath expressions to locate elements on web pages. Ensure that the XPaths are updated if the website structure changes.
- Adjust the file paths and encoding as needed for your system.

