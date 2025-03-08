import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import parser

#====================Your Linkedin Credential==============================
LINKEDIN_EMAIL = "Your email"
LINKEDIN_PASSWORD = "Your password"
#==========================================================================


def human_delay():
    time.sleep(random.uniform(2, 5))  


def init_driver():
    options = webdriver.ChromeOptions()
    options.headless = False  # visible mode so you can see what happens
    options.add_argument("start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")  
    driver = webdriver.Chrome(options=options)
    return driver

# Log in to LinkedIn
def login_linkedin(driver):
    driver.get("https://www.linkedin.com/login")
    human_delay()

    email_box = driver.find_element(By.ID, "username")
    email_box.send_keys(LINKEDIN_EMAIL)
    human_delay()

    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys(LINKEDIN_PASSWORD)
    human_delay()

    password_box.send_keys(Keys.RETURN)
    human_delay()
    
    print("✅ Successfully logged into LinkedIn!")

# search Google for LinkedIn Profile
def search_google(name, school, driver):
    query = f'site:linkedin.com/in/{name} {school}'
    print(f"🔍 Searching Google for: {query}")

    driver.get("https://www.google.com")
    human_delay()

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    human_delay()

    search_box.send_keys(Keys.RETURN)
    human_delay()


    search_results = driver.find_elements(By.XPATH, "//h3/ancestor::a")
    if search_results:
        profile_link = search_results[0].get_attribute("href")
        print(f"✅ Found LinkedIn profile: {profile_link}")
        driver.get(profile_link)
        human_delay()
        return profile_link
    else:
        print(f"❌ No LinkedIn profile found for {name}")
        return None

def extract_profile_text(driver):
    try:
        body_element = driver.find_element(By.TAG_NAME, "body")
        text = body_element.text
        return text
    except Exception as e:
        print(f"⚠️ Error extracting text: {e}")
        return ""

def main():
    driver = init_driver()
    login_linkedin(driver)
    
    
    
    results = {}
    print(json.dumps(parser.people,indent=4))
    for person in parser.people:
        print("=" * 50)
        print(f"Searching for: {person['name']} from {person['school']}")
        print("=" * 50)
        
        profile_link = search_google(person["name"], person["school"], driver)
        if profile_link:
            profile_text = extract_profile_text(driver)
            results[person["name"]] = {
                "profile_link": profile_link,
                "text": profile_text
            }
    
    driver.quit()
    
    # Save all results into a JSON file
    output_json_path = "results.json"
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Data saved to {output_json_path}")

if __name__ == "__main__":
    main()
