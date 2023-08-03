# Generic models
class Config:
    key: str
    check_connection_endpoint: str


class PluginModel:

    def __init__(self, config: Config):
        self.config = config

    def check_connection(self):
        pass


