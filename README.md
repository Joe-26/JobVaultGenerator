# Project Name: **JobVaultGenerator**

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [Installation Guide](#installation-guide)
5. [To Do](#to-do)

## Project Overview

**JobVaultGenerator** is a Python-Selenium automation app that can create folders for jobs and place the respective resume, CV, and job description files for our records.

Resources


## Key Features
1. Makes a company folder, and a Job Folder with a Sample CV, Resume, and Job Description image.
2. Helps keep the records so they can be referred to in case selected for further rounds.

## Technologies Used
1. Python
2. Selenium

## Installation Guide
Follow these steps to get your project up and running locally.

### Prerequisites:
- Python 3.x
- pip (Python package installer)
- Virtual Environment (optional but recommended)


1. Open a terminal & Clone the `JobVaultGenerator` repository from GitHub:
   ```bash
   git clone https://github.com/Joe-26/JobVaultGenerator.git
   ```
   
2. Create a virtual environment called `venv` using Python:
   ```bash
   python3 -m venv venv
   ```
   
3. Activate the virtual environment to isolate your project dependencies:
   ```bash
   source venv/bin/activate
   ```

4. Change to the `JobVaultGenerator` directory:
   ```bash
   cd JobVaultGenerator
   ```

5. Install the required Python dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

6. Change the `path` variable in the main function in `main.py` where you want all the Company folders to be created.
7. There is a `resume_store` folder, where you can place 4 resumes targeting different roles.
8. In case, you need to change the names of the resumes in the resume_store, you'll also need to change the `copy_files` function and resume_num input message accordingly.

## To do
Integrate the OpenAI API for generating the CV Content according to the job description and the profile.
