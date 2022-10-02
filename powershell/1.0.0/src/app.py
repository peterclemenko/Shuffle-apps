import time
import json
import socket
import asyncio
import requests
import subprocess
        
from walkoff_app_sdk.app_base import AppBase

class Powershell(AppBase):
    __version__ = "1.0.0"
    app_name = "Powershell"    # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        self.headers = {"Content-Type": "application/json"}
        super().__init__(redis, logger, console_logger)


    def execute_powershell(self, code):
        powershell_execute = subprocess.run(["pwsh", code])
        
        """
        Returns log of what was executed
        """
        message = f"powershell code {code} has been executed"

        # This logs to the docker logs
        self.logger.info(message)
        return powershell_execute[0]

if __name__ == "__main__":
    Powershell.run()
