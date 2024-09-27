# Backend 

# FLASK API
## Description

This is a Flask Restful API application designed to manage requests to Deepface Deepl Learning model, and provide response to frontend application. This README provides instructions for setting up the application, running it locally.

## Features

- Route compare to compare two images
- Route comparedata to find an image in images database

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- Flask, Deepface and other dependencies listed in requirements.txt

## Installation

Follow these steps to set up the application on your local machine:

1. *Clone the repository:*
```sh
git clone git@github.com:iSheero-AI/ATUT24-DataScience-G1-SimFace.git

cd backend
```
   

2. *Create a virtual environment:*

```sh
python3 -m venv virtual_env_name
source virtual_env_name/bin/activate  
   # On Windows use `virtual_env_name\Scripts\activate`
```

3. *Install the required packages:*

```sh
pip install -r requirements.txt  
```

or 

```sh
cd deepface
pip install -e .
```

## Usage

To run the application locally:

```sh
flask run
```

Visit http://127.0.0.1:5000/ in your browser to see the application in action.