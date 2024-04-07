# XML Command Management System

## Introduction

XML Command Management System is a Flask-based application that allows users to manage commands in XML format. Users can add new commands, validate them against an XSD schema, and view or delete existing commands.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Flask application:
   ```bash
   flask run

4. Access the application in your web browser at http://localhost:5000.

## Usage
  - Add Order: Navigate to /add-order to add a new order. Fill in the client information and product details, then click "Submit" to generate the XML command.

  - View Commands: Navigate to /command-list to view a list of existing commands. Click on a command to view its details.

  - Delete Command: From the command list, click "Delete" next to a command to delete it.
    
## Dependencies
  - Flask
  - xmlschema
  - xml.etree.ElementTree
  - os
  - datetime

## Folder Structure
  - static/: Contains static files such as CSS, XML schemas, and XML files.
  - templates/: Contains HTML templates used by Flask for rendering pages.
  - app.py: The main Flask application file.
  - requirements.txt: List of Python dependencies.
