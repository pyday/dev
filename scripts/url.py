# -*- coding: utf-8 -*-
# import urlparse
import ping, socket
import threading


# class Pinger(object):
#     def __init__(self, hosts):
#         for host in hosts:
#             hostname = urlparse.urlparse(host).hostname
#             if hostname:
#                 pa = PingAgent(hostname)
#                 pa.start()
#             else:
#                 continue

def pingIp(ip):
    try:
        p = ping.do_one(ip, timeout=2, psize=8)
        return p
        # delay = ping.Ping('www.wikipedia.org', timeout=2000).do()
    except socket.error, e:
        # print "Ping Error:", e
        pass


if __name__ == '__main__':
    import csv

    with open('ips.csv', 'wb') as csvfile:
        fieldnames = ['ip', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        threads = []
        for i in range(255):
            def target():
                current = i
                url = "x.x.x.%d" % current
                p = pingIp(url)

                if p:
                    writer.writerow({'ip': url, 'time': p * 1000})
                # else:
                #     print "current:%d,time:%s" % (url, p)


            thread = threading.Thread(target=target)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()
