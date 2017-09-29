#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generatepom import PomXMLTemplate
from flask import send_file, request
from instance.config import app_config
from flask_cors import CORS, cross_origin
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
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)

    @app.route('/generatefile', methods=['POST'])
    @cross_origin()
    def generatefile():
        return send_file(PomXMLTemplate(dict(request.get_json())).xml_file(),
                         attachment_filename=MANIFEST_FILE['maven'],
                         as_attachment=True)
    return app
