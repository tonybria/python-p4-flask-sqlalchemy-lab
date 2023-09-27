#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    """
    Handle requests to the homepage.
    Returns:
        Response: A Flask Response object with a welcome message.
    """
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    return ''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''
@app.route('/animal/<int:num>')
def animal_by_id(num):
    """
    Handle requests to display information for an animal by its ID.
    Args:
        num (int): The ID of the animal to display.
    Returns:
        Response: A Flask Response object with animal information.
    """
    animal = Animal.query.filter(Animal.id == num).first()

    response_body = f"""
        <ul>ID: {animal.id}</ul>
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper.name}</ul>
        <ul>Enclosure: {animal.enclosure.environment}</ul>    
    """
    return make_response(response_body, 200)


@app.route('/zookeeper/<int:num>')
def zookeeper_by_id(num):
    """
    Handle requests to display information for a zookeeper by their ID.
    Args:
        num (int): The ID of the zookeeper to display.
    Returns:
        Response: A Flask Response object with zookeeper information.
    """
    zookeeper = Zookeeper.query.filter(Zookeeper.id == num).first()

    animal_names_html = ""
    for animal in zookeeper.animals:
        animal_names_html += f"<ul>Animal: {animal.name}</ul>"

    response_body = f"""
        <ul>ID: {zookeeper.id}</ul>
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>
        {animal_names_html}
    """

    return make_response(response_body, 200)


@app.route('/enclosure/<int:num>')
def enclosure_by_id(num):
    """
    Handle requests to display information for an enclosure by its ID.
    Args:
        num (int): The ID of the enclosure to display.
    Returns:
        Response: A Flask Response object with enclosure information.
    """
    enclosure = Enclosure.query.filter(Enclosure.id == num).first()

    animal_names_html = ""
    for animal in enclosure.animals:
        animal_names_html += f"<ul>Animal: {animal.name}</ul>"

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''
    response_body = f"""
        <ul>ID: {enclosure.id}</ul>
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
        {animal_names_html}
    """
    return make_response(response_body, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)