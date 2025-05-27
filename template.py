# File which will make the complete project structure (this file will have all the logic)

import os
from pathlib import Path
import logging

logging.basicConfig(
format ="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level =logging.INFO,
)

project_name = "TextSummarizer"  # Prject structure creating

list_of_file =[                  # List of file & structure
    ".github/workflows/.gitkeep",  # this we use for CI/CD deployment . Here we will be writing Yaml code so whenever we do commit , it will deploy it in cloud. .gitkeep is temporary file as wecannot create empty folder. When we will create yaml file we will delete it.
    f"src/{project_name}/__init__.py", # Init.py is required so that we can install it as Local Package
    f"src/{project_name}/components/__init__.py", # creating Component folder which will also have init.py
    f"src/{project_name}/utils/__init__.py",  # Utils will also have init.py
    f"src/{project_name}/utils/common.py",  # In common file we will use write utility
    f"src/{project_name}/logging/__init__.py", # Creating Logging folder having init.py file
    f"src/{project_name}/config/__init__.py", #  Creating config folder having init.py file
    f"src/{project_name}/config/configuration.py", # In configuration file we will write configuration
    f"src/{project_name}/pipeline/__init__.py" # Creating Pipleine folder with init file
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # This is another configuration folder with config.yaml file
    "params.yaml", # This will have all model related parameter
    "app.py", # For running python application from local host
    "main.py",
    "Dockerfile", # To build docker image of source code and delpoy that image in EC2 instance of AWS
    "requirements.txt", # Contain all the requirements
    "setup.py", # Having details about the project 
    "research/trails.ipynb" # it contain all the notebook experiment, for EDA

]

## Below is logic so that it will create the project structure

for filepath in list_of_file:
    filepath = Path(filepath) # It will see the operating system and convert the filepath into os file path i.e if its linux then f"src/{project_name}/__init__.py" will change to f"src\{project_name}\__init__.py". basicaly forward slash will change to backward slash
    filedir,filename= os.path.split(filepath) # It will split the folder and file seprately i.e file directory = src/{project_name}/ & file_name = __init__.py

    if filedir != "": # checking if filedirectory is not empty , if file directory is empty then we are not running below logic
        os.makedirs(filedir,exist_ok= True) # creating directory , exist_ok = True means if there is no folder then it will create a folder if there is folder then it wont create it
        logging.info(f"Creating directory:{filedir} for the file {filename}") # Logging folder creation 

    #After Folder creation , now we will create file inside the folder created

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # Checking if file is not existing by check the file path that is if file path dont exist that means file also dont exist and 2nd condition is checking if file path but its with empty file (file size is 0) , then we will create a file
        with open(filepath,"w") as f:            # Opening in writing mode
            pass
            logging.info(f"creating empty file: {filepath}")


    else:
        logging.info(f"{filename} already exist")

        




