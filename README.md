# flask-blog-tutorial
Flask tutorial

# Flaskr Tutorial

Flaskr is a simple blog application that allows users to register, log in, create posts, and edit or delete their own posts. It is based on the official Flask tutorial², but with some modifications and improvements. This README will guide you through setting up and running Flaskr on your local machine.

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.11.2 or higher
- pip
- git

## Installation

To install Flaskr, follow these steps:

- Clone this repository to your local machine:

```bash
git clone https://github.com/shahbaz42/flask-blog-tutorial.git
```

- move to the project directory
```bash
cd flask-blog-tutorial
```

- Create a virtual environment and install dependencies:
```bash
python -m venv venv
```

- Activate the virtual environment:
```bash
source venv/Source/activate
```

- Install required dependencies
```bash
pip install -r requirements.txt
```

## Initialization
To initialize Flaskr, you need to create the database schema and some initial data. Run this command:

```bash
flask init-db
```

This will create a file called `flaskr.sqlite` in the `instance` folder, which is where Flask stores files that are not meant to be shared with others.

## Running
- To run Flaskr, use this command:

```bash
flask --app flaskr run 
```

- To run Flasker in debug mode
```bash
flask --app flaskr run --debug
```

This will start a development server on http://localhost:5000. You can visit this URL in your browser and see the Flaskr homepage.

You can log in or register a new user.

You can create new posts by clicking on "New" in the navigation bar.

You can edit or delete your own posts by clicking on "Edit" or "Delete" below each post.
