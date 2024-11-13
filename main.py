import click
import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def copy_files(path, resume_num, company, job_folder):
    # Copy resume.docx to Job folder
    if resume_num == 1:
        shutil.copy(path+'resume_store/devops.docx', path+company+'/'+job_folder+'/'+'Joseph_2024.docx')
    elif resume_num == 2:
        shutil.copy(path+'resume_store/data.docx', path+company+'/'+job_folder+'/'+'Joseph_2024.docx')
    elif resume_num == 3:
        shutil.copy(path+'resume_store/pythondev.docx', path+company+'/'+job_folder+'/'+'Joseph_2024.docx')
    elif resume_num == 4:
        shutil.copy(path+'resume_store/javadev.docx', path+company+'/'+job_folder+'/'+'Joseph_2024.docx')
    elif resume_num == 5:
        shutil.copy(path+'resume_store/cloud.docx', path+company+'/'+job_folder+'/'+'Joseph_2024.docx')
    
    # Copy cv.docx to Job folder
    shutil.copy(path+'Joseph_24_CL.docx', path+company+'/'+job_folder)

    # Copy jd.pdf to Job folder
    shutil.copy(path+'JD.png', path+company+'/'+job_folder)


def make_jd_file(jobLink):
    options = Options()
    options.headless = True
    
    # Initialize the WebDriver
    driver = webdriver.Firefox(options=options)

    # Open link
    driver.get(jobLink)
    time.sleep(5)

    driver.get_full_page_screenshot_as_file('JD.png')
    time.sleep(2)    
    
    # Get the entire page content and save it to a text file
    page_text = driver.find_element("tag name", "body").text
    with open('JD.txt', 'w', encoding='utf-8') as f:
        f.write(page_text)

    driver.quit()


"""
def get_job_desc(jobLink):
    job_description = ''
    
    # Make a JD.pdf and place in root location
    make_jd_file(jobLink)

    return job_description
"""


def folder_present(path, company_folder):
    return os.path.exists(path+company_folder)


@click.command()
@click.option('--job_link', required=True, help='Enter the Job Link')
def main(job_link):
    path = '/Users/joseph/Documents/PythonProjects/JobVault/'
    data = {}
    data["company"] = input('Enter Company Name: \n')
    data["job_link"] = job_link
    data["job_id"] = input('Enter Job Id: \n')
    data["position"] = input('Enter Position: \n')
    data["resume_num"] = int(input('Which Resume?(enter number) \n1. DevOps \n2. Data \n3. PythonDev \n4. JavaDev \n5. Cloud\n'))


    # Get Job Details from the website
    data["job_desc"] = make_jd_file(data['job_link'])

    # Check Company name folder
    if (not folder_present(path, data["company"])):
        # Make Company folder
        os.mkdir(path+data['company'])

    
    # Make Job Folder
    job_folder = data['job_id']+' '+data['position']
    os.mkdir(path+data['company']+'/'+job_folder)
    
    # Copy files
    copy_files(path, data['resume_num'], data['company'], job_folder)


if __name__ == '__main__' :
    main()
