# Building your project as a reusable package like seaborn , pandas and can deploy on cloud or PyPi in future 

from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines() if line.strip() and not line.strip().startswith('#')]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='Student_Performance_Prediction',
    version='0.0.1',
    author='Bhavesh Solanki',
    author_email='bhaveshsolankibj960@gmail.com',
    packages=find_packages(), # find all folder with __init__.py file name , this folder is package
    install_requires=get_requirements('requirements.txt')  # path to requirements.txt
)
