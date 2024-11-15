import click
import os
import shutil
import time
from docx import Document
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def make_cv(data):
    print(data['cv_info'].items())
    doc = Document('CV_template.docx')
    for paragraph in doc.paragraphs:
        for placeholder, value in data['cv_info'].items():
            for run in paragraph.runs:
                if placeholder in run.text:
                    run.text = run.text.replace(placeholder, value)
        
    doc.save('CV.docx')

def copy_files(path, resume_num, company, job_folder):
    # Copy resume.docx to Job folder
    if resume_num == 1:
        shutil.copy('resume_store/devops.docx', path+company+'/'+job_folder+'/Joseph_2024.docx')
    elif resume_num == 2:
        shutil.copy('resume_store/data.docx', path+company+'/'+job_folder+'/Joseph_2024.docx')
    elif resume_num == 3:
        shutil.copy('resume_store/pythondev.docx', path+company+'/'+job_folder+'/Joseph_2024.docx')
    elif resume_num == 4:
        shutil.copy('resume_store/javadev.docx', path+company+'/'+job_folder+'/Joseph_2024.docx')
    elif resume_num == 5:
        shutil.copy('resume_store/cloud.docx', path+company+'/'+job_folder+'/Joseph_2024.docx')
    
    # Copy cv.docx to Job folder
    shutil.move('CV.docx', path+company+'/'+job_folder+'/CV.docx')

    # Copy jd.pdf to Job folder
    shutil.move('JD.png', path+company+'/'+job_folder)

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
    
    # Get the entire page content 
    page_text = driver.find_element("tag name", "body").text

    # save it to a text file
    """
    with open('JD.txt', 'w', encoding='utf-8') as f:
        f.write(page_text)
    """
    
    driver.quit()
    return(page_text)

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
    data["cv_info"] = {
        '{NAME}': 'firstname lastname',
        '{LOCATION}': 'Okemos, MI',
        '{MOBILE}': '(123)-456-7890',
        '{EMAILID}': 'name@gmail.com',
        '{DATE}': '14 November, 2024',
        '{COMPANY}': str(data['company'])
    }

    # Get Job Details from the website
    data["job_desc"] = make_jd_file(data['job_link'])

    # Add data to CV_template  
    make_cv(data)

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
