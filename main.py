from flask import Flask, render_template, request, redirect, url_for, session
import xml.etree.ElementTree as ET
from xmlschema import XMLSchema
import datetime
import os

app = Flask(__name__)
app.secret_key = "very_secret_key_don't_share_lol"
xsd_schema = XMLSchema('static/XML_schema/XSD.xsd')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-order')
def add_order():
    return render_template('add_order.html')

@app.route('/generate_xml', methods=['POST'])
def generate_xml():
    root = ET.Element("commande")
    client = ET.SubElement(root, "client")
    client_nom = request.form['client_nom']
    ET.SubElement(client, "nom").text = client_nom
    client_prenom = request.form['client_prenom']
    ET.SubElement(client, "prenom").text = client_prenom
    client_adresse = request.form['client_adresse']
    ET.SubElement(client, "adresse").text = client_adresse
    client_ville = request.form['client_ville']
    ET.SubElement(client, "ville").text = client_ville
    client_code_postal = request.form['client_code_postal']
    ET.SubElement(client, "code_postal").text = client_code_postal
    produits = ET.SubElement(root, "produits")
    produit_noms = request.form.getlist('produit_nom[]')
    produit_quantites = request.form.getlist('produit_quantite[]')
    produit_prix_unitaires = request.form.getlist('produit_prix_unitaire[]')
    for i in range(len(produit_noms)):
        produit = ET.SubElement(produits, "produit")
        ET.SubElement(produit, "nom").text = produit_noms[i]
        ET.SubElement(produit, "quantite").text = produit_quantites[i]
        ET.SubElement(produit, "prix_unitaire").text = produit_prix_unitaires[i]
    tree = ET.ElementTree(root)
    file_name = "static/commands/{}.xml".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    tree.write(file_name)
    is_valid = xsd_schema.is_valid(file_name)
    if is_valid:
        session['file_name'] = file_name 
        return redirect(url_for("success"))
    else:
        return redirect(url_for("error"))

@app.route('/success')
def success():
    file_name = session.pop('file_name', None) 
    if file_name:
        with open(file_name, "r") as xml_file:
            xml_content = xml_file.read()
        return render_template('success.html', xml_file=file_name, xml_content=xml_content)
    else:
        return "File not found"

@app.route('/error')
def error():
    return render_template('error.html', error="Invalid XML format")

@app.route('/command-list')
def command_list():
    folder_path = "static/commands"
    xml_files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.xml')]
    return render_template('command_list.html', xml_files=xml_files)

@app.route('/command-list/open/<id>')
def open_xml(id):
    file_path = os.path.join("static/commands", id + '.xml')
    if os.path.exists(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        client_elem = root.find('client')
        client = {
            'nom': client_elem.find('nom').text,
            'prenom': client_elem.find('prenom').text,
            'adresse': client_elem.find('adresse').text,
            'ville': client_elem.find('ville').text,
            'code_postal': client_elem.find('code_postal').text
        }
        produits_elem = root.find('produits')
        produits = []
        for produit_elem in produits_elem.findall('produit'):
            produit = {
                'nom': produit_elem.find('nom').text,
                'quantite': produit_elem.find('quantite').text,
                'prix_unitaire': produit_elem.find('prix_unitaire').text
            }
            produits.append(produit)

        return render_template('result.html', client=client, produits=produits)
    else:
        return 'File not found'

@app.route('/delete/<id>')
def delete(id):
    file_path = os.path.join("static/commands", id + '.xml')
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('command_list'))

if __name__ == '__main__':
    app.run(debug=True)
