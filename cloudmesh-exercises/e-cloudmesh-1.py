# fa20-516-238 E.Cloudmesh.Common.1

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE


class CloudmeshCommon:

    def __init__(self, str):
        self.str = str

    def demo_banner(self):
        banner(self.str)

    def demo_heading(self):
        HEADING(self.str)

    def demo_verbose(self):
        test_dict = {"INDIA":"New Delhi",
                     "GERMANY":"Berlin",
                     "USA":"Washington D.C.",
                     "UK":"London"}
        VERBOSE(test_dict)

if __name__ == '__main__':
    demo = CloudmeshCommon("This is demo text")
    demo.demo_banner()
    demo.demo_heading()
    demo.demo_verbose()