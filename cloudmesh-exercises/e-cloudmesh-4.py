# fa20-516-238 E.Cloudmesh.Common.5

from cloudmesh.common.util import banner
from cloudmesh.common.Shell import Shell

class CloudmeshCommon:

    def demo_shell(self):
        #get python and pip version from virtual environment
        python, pip  = Shell.get_python()
        #check for latest Python version
        if python == '3.8.1':
            print("You have installed the latest Python version.\n")
        else:
            print("You Python version is:",python)
            print("Please upgrade to latest Python version.\n")
        #Check for latest pip version
        if pip =='20.0.2':
            print("You have installed the latest pip version.\n")
        else:
            print("You pip version is:", pip)
            print("Please upgrade to latest pip version.\n")

if __name__ == '__main__':
    demo = CloudmeshCommon()
    banner("Shell Demo",c="x",prefix="$",color="GREEN")
    demo.demo_shell()