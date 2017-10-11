# ITS Project Server - Group I

## Introduction

The repository contains the codes for the server side of the ITS Project. The project has been made using **Django Framework**. It consists of the models, serializers, views and settings of the project. 

## Installation

The server side needs some dependencies to build the project. It is recommended to use _virtualenv_ to install the dependencies. The installation guide is works for Ubuntu 16.04 at the time of writing.

First, clone this repository, with link provided [here](https://github.com/vaishnavm217/itsprojectserver.git). Then follow one of the following methods:

1. Installing dependencies using _Virtualenv_ (recommended)

    a. Install pip and virtualenv by issuing the following command: <br>
        ```sudo apt-get install python3-pip python3-dev python-virtualenv```.
    
    b. Create a virtualenv environment by issuing the following command: <br>
          ```virtualenv --system-site-packages -p python3 targetDirectory``` <br> <br> where targetDirectory specifies the top of the virtualenv tree. Our instructions assume that targetDirectory is ```~/python3-its```, but you may choose any directory.
          
    c. Activate the virtualenv environment by issuing the following command: <br>
          ```source ~/python3-its/bin/activate```. <br><br> The preceding source command should change your prompt to the following:<br>
          ```(python3-its)$ ```
          
    d. Then, go to the downloaded repository _itsprojectserver_ and run the following command: <br>
        ```pip install -r requirements.txt```. <br><br> It will install all the required dependencies in [requirements.txt](https://github.com/vaishnavm217/itsprojectserver/blob/master/requirements.txt).
  
2. Installing directly to the system
    
    - Go to the downloaded repository _itsprojectserver_ and run the following command: <br>
        ```pip install -r requirements.txt```. <br><br> It will install all the required dependencies in [requirements.txt](https://github.com/vaishnavm217/itsprojectserver/blob/master/requirements.txt).
        
## Usage


    
    
