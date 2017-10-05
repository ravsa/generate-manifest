#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GenerateManifest import PomXMLTemplate
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
        return send_file(PomXMLTemplate(request.get_json()).xml_file(),
                         attachment_filename=MANIFEST_FILE['maven'],
                         as_attachment=True)

    @app.route('/test', methods=['GET'])
    def testing():
        json_data = {
            "ecosystem": "maven",
            "framework": "springboot",
            "version": "null or 1.2.1",
            "project": {
                "name": "project1",
                "description": "sample description",
                "options": {
                    "group": "group name",
                    "artifactId": "Id of artifact",
                    "version": "vesion number"
                }
            },
            "dependencies": [
                "Dependency1GroupID:Dpendency1ArtifactID:Dpendency1Version",
                "Dependency2GroupID:Dpendency2ArtifactID",
                "Dependency3"
            ]
        }
        return send_file(PomXMLTemplate(json_data).xml_file(),
                         attachment_filename=MANIFEST_FILE['maven'],
                         as_attachment=True)
        #  return send_file('../pom.xml',
        #                   attachment_filename=MANIFEST_FILE['maven'],
        #                   as_attachment=True)

    return app
