<h1 align="center"> LINEA </h1>

<h4 align="center"> An application with the objective of consume an json and format his data. </h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a>
</p>

## Key Features

* Receive Json data.
* Format this data
* Provide sort and search functions.

## How To Use

To clone and run this script, you'll need [Git](https://git-scm.com), [Python](https://www.python.org) installed on your environment. From your command line:

### Cloning and installing

```bash
# Clone this repository
$ git clone  https://github.com/Lucas-Finatti/LIneA.git

# Go into the repository folder
$ cd: LINEA

# Create your virtualenv
$ Python -m venv env

# Activate env
$ cd: "./env/Scripts/Activate.ps1"

# Install dependencies
$ pip install -r requirements.txt

```

# Usage exemple in Insomnia 

### To make the requests you have to put on insomnia request the token who as defaut is:
'V9yoEjgtt7iUaQP3I4tHrWyIpSJjNQK75Wwjfaj2Se1ch60OsqeFBxo9HUkHn0YC8DjU6lnt7idPpxhvve6yzPy62cf7c2057224'

![image](https://user-images.githubusercontent.com/77365066/178883893-0cb15c4e-e63d-4b23-876a-63039d4bf8b3.png)


### With the Query parameters send the type of request:
Below is an example of how to use the script.

#### If you just want the json data formated you can use: 
http://127.0.0.1:8000/api/?type_function=all&type_param=null&param=null

Your return will be:

![image](https://user-images.githubusercontent.com/77365066/178876666-26771195-2f5a-47ad-ab64-b5d77fcfe4b1.png)

#### If you want to Sort this data use: 
http://127.0.0.1:8000/api/?type_function=sort&type_param=id&param=null

put type_function as sort and type_param value by what you want to sort.  

In this case the return will be:

![image](https://user-images.githubusercontent.com/77365066/178879876-24f8bd67-241f-4ced-8ec2-7913ddb5a9d4.png)

#### if you want to Search an expecficly object use: 
http://127.0.0.1:8000/api/?type_function=search&type_param=id&param=3

put type_function as search, type_param and param value by what you want to search. 

In this case the return will be:

![image](https://user-images.githubusercontent.com/77365066/178882372-72c05dae-5489-492f-b243-10aec6f75285.png)

## How to change the API Url/Token.

#### To change the token or API url change de vars in enviroments.py:

![image](https://user-images.githubusercontent.com/77365066/178884189-8c72383b-d3ab-43eb-9b94-df7ac319f1b0.png)

## Credits

This software uses the following open source packages:

- [Django RestFramework](https://www.django-rest-framework.org)
- [Django](https://www.djangoproject.com)
