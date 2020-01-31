
APP_CONFIG_MAPPER = {
        'development': 'config_sample.DevelopmentConfig',
        'production': 'config_sample.ProductionConfig',
        'local': 'config_sample.LocalConfig'
}


class BaseConfig(object):
    """
    Base config class
    """
    DEBUG = True
    TESTING = False


class LocalConfig(object):
    """
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = False
    MONGO_DB_URI = "mongodb://root:password@your_local_db"


class DevelopmentConfig(object):
    """
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = True
    MONGO_DB_URI = "mongodb://root:password@your_dev_db"


class ProductionConfig(object):
    """
    Production specific config
    """
    DEBUG = True
    MONGO_DB_URI = "mongodb://root:password@your_prod_db"