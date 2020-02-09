# fa20-516-238 E.Cloudmesh.Common.3

from cloudmesh.common.util import banner
from cloudmesh.common.FlatDict import FlatDict

class CloudmeshCommon:

    def demo_flatdict(self):
        test_dict = {"country": "UNITED STATES OF AMERICA",
                     "attributes": {
                         "Language": "English",
                         "Capital": "Washington D.C.",
                         "Currency":"USD"
                     }
                     }
        print(test_dict)
        flat_list = FlatDict(test_dict,sep=".")
        banner("Flattened list for test_dict")
        print(flat_list)


if __name__ == '__main__':
    demo = CloudmeshCommon()
    banner("FlatDict Demo")
    demo.demo_flatdict()