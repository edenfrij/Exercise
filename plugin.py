import requests
from models import PluginModel


# Generic plugin
class Plugin(PluginModel):

    def __init__(self, config):
        super().__init__(config)

    # Connectivity test
    def check_connection(self):
        response = requests.get(self.config.check_connection_endpoint, headers={"app-id": self.config.key})
        if response.status_code == 200:
            print("Connection established", response.status_code)
        else:
            print("Connection failed", response.status_code)



















