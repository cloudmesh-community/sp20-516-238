# fa20-516-238 E.Cloudmesh.Common.2

from cloudmesh.common.util import banner
from cloudmesh.common.dotdict import dotdict

class CloudmeshCommon:

    def demo_dotdict(self):
        student = { "name":"Ishan Mishra",
                    "id":"238",
                    "subject":"ECC"
                    }
        student = dotdict(student)

        print("Student Name:",student.name,"\n")
        print("Student ID:", student.id,"\n")
        print("Subject Enrolled:", student.subject,"\n")

if __name__ == '__main__':
    demo = CloudmeshCommon()
    banner("\t\t Student's Details",c="x", prefix="@")
    demo.demo_dotdict()