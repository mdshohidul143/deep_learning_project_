# from setuptools import find_packages,setup
# from typing import List

# HYPEN_E_DOT='-e .'

# def get_requirements(file_path:str)->List[str]:
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements


# setup(

# name="Xray",
# version="0.0.1",
# author="mdshohidul143",
# author_email="mdshohidulislam01311@gmail.com",
# install_requires=get_requirements(r"C:\\Users\\Juwel\\deep_learning_project_\\requirements_dev.txt"),
# package=find_packages()

# )
from setuptools import setup, find_packages

setup(
    name='Xray',
    version='1.0.0',
    packages=find_packages(),  # Specify the packages to include
    # Alternatively, you can specify individual modules using py_modules
    # py_modules=['module1', 'module2'],
    # Include other relevant metadata as needed
)


