#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  from StringIO import StringIO
from lxml import etree
from uuid import uuid4
import os


class PomXMLTemplate(object):

    def __init__(self, json_data=None):
        if json_data:
            self._data = json_data
        else:
            raise ValueError("JSON Data is not available")
        self.root = etree.Element(
            'project',
            xmlns="http://maven.apache.org/POM/4.0.0",
        )
        self.tree = etree.ElementTree(self.root)
        self.create()

    def create(self):
        self._project = self._data.get('project', None)
        if self._project:
            self._options = self._project.get('options', None)
            etree.SubElement(self.root, 'modelVersion').text = '4.0.0'
            if self._options:
                etree.SubElement(self.root, 'groupId').text = self._options.get(
                    'group', None)
                etree.SubElement(self.root, 'artifactId').text = self._options.get(
                    'artifactId', None)
                etree.SubElement(self.root, 'version').text = self._options.get(
                    'version', None)
            etree.SubElement(self.root, 'packaging').text = 'pom'
            etree.SubElement(self.root, 'description').text = self._options.get(
                'description', None)
            etree.SubElement(self.root, 'url').text = 'https://example.com'
            self.licenses = etree.SubElement(self.root, 'licenses')
            self.license = etree.SubElement(self.licenses, 'license')
            etree.SubElement(
                self.license, 'name').text = "Apache License, Version 2.0"
            etree.SubElement(
                self.license, 'url').text = "http://www.apache.org/licenses/LICENSE-2.0"
            self.parent = etree.SubElement(self.root, 'parent')
            etree.SubElement(
                self.parent, 'groupId').text = "org.springframework.boot"
            etree.SubElement(
                self.parent, 'artifactId').text = "spring-boot-starter-parent"
            etree.SubElement(self.parent, 'version').text = "1.3.2.RELEASE"
            self.append_dependencies(self._data['dependencies'])

    def append_dependencies(self, dependencies):
        self.dpmanage = etree.SubElement(self.root, "dependencyManagement")
        self.dps = etree.SubElement(self.dpmanage, "dependencies")
        for item in dependencies:
            dp = etree.SubElement(self.dps, 'dependency')
            temp = item.split(':')
            if len(temp) == 1 or len(temp) > 3:
                etree.SubElement(dp, 'groupId').text = item
            elif len(temp) == 2:
                etree.SubElement(dp, 'groupId').text = temp[0]
                etree.SubElement(dp, 'artifactId').text = temp[1]
            else:
                etree.SubElement(dp, 'groupId').text = temp[0]
                etree.SubElement(dp, 'artifactId').text = temp[1]
                etree.SubElement(dp, 'version').text = temp[2]

    def xml_file(self):
        path = os.path.join('/tmp', uuid4().hex)
        with open(path, 'w') as file:
            self.tree.write(file, encoding='utf-8', xml_declaration=True, pretty_print=True)
        return path
