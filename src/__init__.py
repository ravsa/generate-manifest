#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generatepom import PomXMLTemplate
from instance.config import app_config
from flask import send_file, request, jsonify
from flask_api import FlaskAPI


MANIFEST_FILE = {
    'maven': 'pom.xml',
    'node': 'packages.json',
    'python': 'requirements.txt'
}


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/generatefile/', methods=['POST', ])
    def generatefile():
        response = jsonify("{'a':'b'}")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        #  return send_file(PomXMLTemplate(dict(request.get_json())).xml_file(),
        #                   attachment_filename=MANIFEST_FILE['maven'],
        #                   as_attachment=True)

    return app
