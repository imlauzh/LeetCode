"""
小美在听歌。歌单给小美推送了一个歌单序列，歌单中的歌会严格按顺序播放。

歌单中有很多歌曲，听每首歌曲会给小美带来ai点愉悦值。但是某些歌曲是一个系列的。如果小美在听这首歌曲之前没有按顺序听过这个系列的所有前面的歌曲，就会给小美带来-bi的愉悦值（即最后选择这首歌可获得的总愉悦值为ai-bi。）歌单并不会保证这首歌在系列中前面的歌曲都在歌单中。

因此，小美可以预先去除中间的一些歌曲，使得自己更加愉悦。由于去掉歌曲需要花费时间，所以每去掉一首歌曲都会让自己的愉悦值减小k。

由于歌单是智能的，所以其中不会包含重复的歌曲。

请问小美能获得的最大愉悦值是多少？
输入描述
第一行两个空格隔开的整数n,k(1≤n,k≤105)代表歌曲数量和删除歌曲减少的愉悦值。

接下来n行每行包括四个空格隔开的整数ai,bi,ci,di(1≤ai,bi,ci,di≤105)分别代表听这首歌获得的愉悦值，没有按顺序听完这个系列之前的歌所需要扣除的愉悦值，这首歌所在的系列，这首歌在系列中是第几首。

输出描述
输出一个数字代表小美能获得的最大愉悦值
样例输入
5 1
20 1000 1 2
1 1 1 1
5 3 1 3
20 1 2 2
22 2 2 3
样例输出
41
"""


class MaxSongs:
    def calc(self, n, k, songs):
        def backTrack(index):
            nonlocal res, p
            if index == n:
                res = max(res, p)
                return
            p -= k
            backTrack(index+1)
            p += k
            if album[songs[index][2]][0][0] < songs[index][3]-1:
                p += songs[index][0]-songs[index][1]
                backTrack(index+1)
                p -= songs[index][0]-songs[index][1]
            elif album[songs[index][2]][0][0] >= songs[index][3]-1:
                p += songs[index][0]
                backTrack(index+1)
                p -= songs[index][0]
        album = dict()
        for s in songs:
            if not album.get(s[2], None):
                album[s[2]] = [(0, 0)]*1000
                album[s[2]][s[3]] = (s[0], s[1])
            else:
                album[s[2]][s[3]] = (s[0], s[1])
        # print(album)
        res = 0
        p = 0
        path = []
        backTrack(0)
        return res

    def calc1(self, n, k, songs):
        album = dict()
        for s in songs:
            if not album.get(s[2], None):
                album[s[2]] = [(0, 0)]*1000
                album[s[2]][s[3]] = (s[0], s[1])
            else:
                album[s[2]][s[3]] = (s[0], s[1])
        res = 0
        for index in range(n):
            if album[songs[index][2]][0][0] < songs[index][3]-1:
                res = max(res-k, res+songs[index][0]-songs[index][1])
            elif album[songs[index][2]][0][0] >= songs[index][3]-1:
                res = max(res-k, res+songs[index][0])
                album[songs[index][2]][0] = (songs[index][3], 0)
        return res

    def calc2(self, n, k):
        res = 0
        listened = {}

        def func(serices, index):
            if index == 1:
                return True
            if serices not in listened:
                return False
            index -= 1
            while index > 0:
                if index not in listened[serices]:
                    return False
                index -= 1
            return True
        for i in range(n):
            a, b, c, d = songs[i]
            if func(c, d):
                cur = a
                if c in listened:
                    listened[c].append(d)
                else:
                    listened[c] = [d]
            else:
                tmp = a-b
                dont = -k
                if tmp > dont:
                    cur = tmp
                    if c in listened:
                        listened[c].append(d)
                    else:
                        listened[c] = [d]
                else:
                    cur = dont
            res += cur
        return res


song = MaxSongs()
n, k = list(map(int, input().strip().split(' ')))
songs = []
for i in range(n):
    a, b, c, d = list(map(int, input().strip().split(' ')))
    songs.append([a, b, c, d])
res = song.calc2(n, k, songs)
print(res)
