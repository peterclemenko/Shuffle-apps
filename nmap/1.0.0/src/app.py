import time
import json
import socket
import asyncio
import subprocess
        
from walkoff_app_sdk.app_base import AppBase

class Nmap(AppBase):
    __version__ = "1.0.0"
    app_name = "Nmap"    # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        self.headers = {"Content-Type": "application/json"}
        super().__init__(redis, logger, console_logger)


    def execute_nmap(self, flags):
        nmap_execute = subprocess.run(["nmap", flags])
        
        """
        Returns log of what was executed
        """
        message = f"powershell code {flags} has been executed"

        # This logs to the docker logs
        self.logger.info(message)
        return nmap_execute[0]

if __name__ == "__main__":
    Nmap.run()
