from dynaconf import LazySettings

settings = LazySettings(
    SETTINGS_FILE_FOR_DYNACONF='settings.yaml;settings.local.yaml',

)
settings.configure()

HOST = settings['HOST']
DATABASE = settings['DATABASE']
PASSWORD = settings['PASSWORD']
PORT = settings['PORT']
USER = settings['USER']
