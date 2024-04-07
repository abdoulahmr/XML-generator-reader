# XML-generator-reader
XML Command Management System
This application allows users to manage commands in XML format, including adding new commands, validating them against an XSD schema, and viewing and deleting existing commands.

Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
flask run
Access the application in your web browser at http://localhost:5000.

Usage
Add Order: Navigate to /add-order to add a new order. Fill in the client information and product details, then click "Submit" to generate the XML command.

View Commands: Navigate to /command-list to view a list of existing commands. Click on a command to view its details.

Delete Command: From the command list, click "Delete" next to a command to delete it.

Dependencies
Flask
xmlschema
Folder Structure
static/: Contains static files such as CSS, XML schemas, and XML files.
templates/: Contains HTML templates used by Flask for rendering pages.
app.py: The main Flask application file.
requirements.txt: List of Python dependencies.
