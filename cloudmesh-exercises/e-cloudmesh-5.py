# fa20-516-238 E.Cloudmesh.Common.5

from cloudmesh.common.util import banner
from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch


class CloudmeshCommon:

    def demo_stopwatch(self):
        count = 1
        StopWatch.start("demo")
        while (count < 5):
            ping = Shell.ping(host='localhost',count=count)
            print(ping)
            count += count
        StopWatch.stop("demo")
        print("\n Total time elapsed:",StopWatch.get("demo", digits = 5))


if __name__ == '__main__':
    demo = CloudmeshCommon()
    banner("Stopwatch Demo", c="x", prefix="#", color="BLUE")
    demo.demo_stopwatch()
