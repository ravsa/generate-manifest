#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = uuid.uuid4().hex


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
