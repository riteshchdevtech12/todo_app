# Creating a Virtual Environment and Running a Django Project

This README provides step-by-step instructions for creating a virtual environment and running a Django project.

## Prerequisites

- Python should be installed on your system. If it is not, please download and install it from the official website: https://www.python.org/downloads/

## Step-by-Step Instructions

1. Install `virtualenv` by running the following command in your terminal or command prompt:


2. Navigate to your project folder and create a virtual environment by running the following command in your terminal or command prompt:


Note: replace `env` with any name of your choice.

3. Activate the virtual environment by running the following command:

- For Windows: 

  ```
  env\Scripts\activate
  ```

- For Unix or Linux:

  ```
  source env/bin/activate
  ```

4. Install dependencies by running the following command:

```commandline
pip install -r requirements.txt
```

6. Navigate to the project directory and run the Django server by running the following command:

7. Once the server is running, you can access the Django project by opening a web browser and navigating to `http://127.0.0.1:8000/`.
