# Classmate LinkedIn Scraper

This repository contains a Python project that uses **Selenium** along with your LinkedIn account to pull information about your classmates. The project workflow is as follows:

- **Input Names (Planned):**  
  In future updates, the tool will import classmate names and school information from Canvas/People.

- **LinkedIn Profile Scraping (Done):**  
  Currently, the script uses Google search queries to locate a classmate's LinkedIn profile by name and school. Once found, it logs into LinkedIn with your account credentials, navigates to the profile, and extracts all visible text—including work experience and project background.

- **Output to Sheets (Planned):**  
  In a future release, the scraped data will be automatically parsed and output into a Google Sheets document for easy review and analysis.

> **Important:**  
> Use this tool responsibly. Scraping LinkedIn data may violate LinkedIn's Terms of Service and data privacy regulations. This project is for educational purposes only, and you are responsible for its use.

## Features

- **Automated LinkedIn Login:**  
  Uses Selenium to log into LinkedIn using your account credentials.

- **Google Search Integration:**  
  Leverages Google to find public LinkedIn profiles based on a classmate's name and school.

- **Data Extraction:**  
  Extracts visible text from a LinkedIn profile page, which includes work experience and project background.

- **Future Enhancements:**  
  - Automatic import of classmate names from Canvas/People.
  - Parsing and exporting the scraped data directly into Google Sheets.

## Requirements

- Python 3.7+
- [Selenium](https://pypi.org/project/selenium/)
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/) that matches your Chrome version

> *For future Google Sheets integration, additional libraries such as `gspread` may be required.*

## Start

- **Your username and password:**  
  - You must change your **Linkedin password** and **username** under **scrape_user.py**.
  - 
- To run the code, directly copy the Canvas data under **People** to ```raw_data``` and your school to ```SCHOOL_NAME``` under ```Parser.py``` :
```bash
python scrape_user.py --run
```
sample input:
![image](https://github.com/user-attachments/assets/b9191cba-7e64-4671-8ffb-818a2ecb907b)
