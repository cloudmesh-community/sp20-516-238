import os
from cloudmesh.common.util import banner

class Provider:

    def __init__(self, name):
        self.name = name

    def find(self):
        banner(f"find available multipass images")
        os.system(f"multipass find")
        print('\n')

    def launch(self):
        banner(f"launch {self.name}")
        os.system(f"multipass launch -n {self.name}")
        print('\n')

    def start(self):
        banner(f"start {self.name}")
        os.system(f"multipass start {self.name}")
        print('\n')

    def stop(self):
        banner(f"stop {self.name}")
        os.system(f"multipass stop {self.name}")
        print('\n')

    def delete(self):
        banner(f"delete {self.name}")
        # delete the instance
        os.system(f"multipass delete {self.name}")

    # Once purged it cannot be recovered.
    def purge(self):
        banner(f"purge")
        os.system(f"multipass purge")
        print('\n')

    def list(self):
        # list instances
        banner("list the launched instance")
        os.system("multipass list")
        print('\n')

    def shell(self):
        banner("open shell on running instance")
        os.system(f"multipass shell")
        print('\n')


if __name__ == "__main__":
    p = Provider("ubuntu-lts")
    p.find()
    p.launch()
    p.list()
    p.stop()
    p.list()
    p.delete()
    p.list()
    p.purge()
    p.list()
