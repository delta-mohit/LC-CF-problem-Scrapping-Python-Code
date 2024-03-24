#Code for txt file-----------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

def clean_text(text):
    cleaned_text = re.sub(r'\n+', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  
    return cleaned_text.strip()  


def scrape_leetcode_problem(link):

    service = Service(executable_path="C:\\Users\\mohit\\Desktop\\WEB_SCRAPPING\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(link)
    time.sleep(2)

    problem_title_element = driver.find_element(By.XPATH,'//a[@class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"]')
    problem_title = clean_text(problem_title_element.text)

    problem_description_element = driver.find_element(By.XPATH,'//div[@class="elfjS"]')
    problem_statement = clean_text(problem_description_element.text)

    driver.quit()

    return problem_title, problem_statement

def scrape_codeforces_problem(link):
    service = Service(executable_path="C:\\Users\\mohit\\Desktop\\WEB_SCRAPPING\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(link)
    time.sleep(2)   
    problem_title_element = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[3]/div[2]/div/div[1]')
    problem_title = clean_text(problem_title_element.text)

    problem_statement_element = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[3]/div[2]/div/div[2]')
    problem_statement = clean_text(problem_statement_element.text)

    input_element = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[3]/div[2]/div/div[3]')
    input_data = clean_text(input_element.text)

    output_element = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[3]/div[2]/div/div[4]')
    output_data = clean_text(output_element.text)

    driver.quit()
    return problem_title, problem_statement, input_data, output_data


def main():
    problem_link = input("Vivek please enter the problem link: ")
    #title, description = scrape_leetcode_problem(problem_link)
    if "leetcode.com" in problem_link:
        title, statement = scrape_leetcode_problem(problem_link)
        with open('leetcode_problem.txt', 'w', encoding='utf-8') as file:
            file.write(f"Problem Title: \n{title}\n\n")
            file.write(f"Problem Description:\n{statement}\n")
    else:
        title, statement, input_data, output_data = scrape_codeforces_problem(problem_link)
        with open('codeforces_problem.txt', 'w', encoding='utf-8') as file:
            file.write(f"Problem Title: \n{title}\n\n")
            file.write(f"Problem Statement:\n{statement}\n\n")
            file.write(f"Input:\n{input_data}\n\n")
            file.write(f"Output:\n{output_data}\n")

    print("Hey Vivek, Scraping and writing to txt file is completed.")

if __name__ == "__main__":
    main()

