"""
3 2
2 1 2
1 3
0
1 1
0 2
"""
import collections


class Systemd:
    def calc(self, depend, services):
        def run(i):
            if i in running:
                return
            stoped.remove(i)
            running.add(i)
            for d in hashmap[i]:
                run(d)

        def stop(i):
            if i in stoped:
                return
            running.remove(i)
            stoped.add(i)
            for d in hashmap[i]:
                stop(d)
        # print(depend,services)
        hashmap = collections.defaultdict(int)
        running = set()
        stoped = set()
        for d in depend:
            hashmap[d[0]] = d[1]
            stoped.add(d[0])
        # print(hashmap)
        for s in services:
            if s[0] == 1:
                run(s[1])
                for k, v in hashmap.items():
                    if s[0] in v:
                        run(k)
            elif s[0] == 0:
                stop(s[1])
                for k, v in hashmap.items():
                    if s[0] in v:
                        stop(k)
            print(len(running))


s = Systemd()
n, q = list(map(int, input().strip().split(' ')))
depend = []
for i in range(n):
    ser = list(map(int, input().strip().split(' ')))
    depend.append([i+1, ser[1:]])
services = []
for i in range(q):
    ser = list(map(int, input().strip().split(' ')))
    services.append(ser)
s.calc(depend, services)
