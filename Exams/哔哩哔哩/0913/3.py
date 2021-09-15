"""
用户分组
时间限制： 3000MS
内存限制： 589824KB
题目描述：
B站用户数量已经达到上亿的规模，为了给用户提供更好的推荐体验，推荐组需要预先对所有的用户进行用户池分类，在相同用户池的用户被认为具有较高的相似性。这里简化下分类规则，假设有用户22和33，如果22关注、点赞、投币，甚至一键三连了33，即认为22和33可以被放入同一个用户池。请注意：自己是可以给自己点赞和投币的哦～



输入描述
首先给出c，代表接下来有c组case。

对于每一组case，首先给出n和m两个数，空格隔开，有0<n<100,000，0<=m<1,000,000。其中n代表用户总数，用户的编号从0开始，依次递增；接下来会有m行，代表m对关系a_i和b_i，空格隔开，表示a_i关注、或点赞、或投币、或一键三连了b_i，有0<=a_i,b_i<n

输出描述
每一组输入结束后，请输出这n个用户将被划分为多少个用户池。


样例输入
4
6 5
0 3
3 1
0 1
4 5
5 4
4 4
0 1
1 2
2 3
3 0
5 4
0 1
3 1
1 3
0 2
22 23
0 1
1 0
2 3
3 2
4 5
5 4
6 7
7 6
8 9
9 8
10 11
11 10
12 13
13 12
14 15
15 14
16 17
17 16
18 19
19 18
20 21
21 20
0 20
样例输出
3
1
2
10
"""


class YiJianSanLian:
    def find(self, res, val):
        for index, lists in enumerate(res):
            if val in lists:
                return index
        return None

    def calc(self, n, m):
        res = []
        actions = dict()
        for i in range(n):
            actions[i] = 0
        for _ in range(m):
            a, b = list(map(int, input().strip().split(' ')))
            actions[a] += 1
            actions[b] += 1
            if not res:
                res.append([a, b])
            else:
                index_a, index_b = self.find(res, a), self.find(res, b)
                if index_a is None and index_b is None:
                    res.append([a, b])
                elif index_a is None and index_b is not None:
                    res[index_b].append(a)
                elif index_a is not None and index_b is None:
                    res[index_a].append(b)
                elif index_a is not None and index_b is not None:
                    if index_a != index_b:
                        if index_a > index_b:
                            tmp = res[index_a]
                            res.pop(index_a)
                            for p in tmp:
                                if p not in res[index_b]:
                                    res[index_b].append(p)
                        else:
                            tmp = res[index_b]
                            res.pop(index_b)
                            for p in tmp:
                                if p not in res[index_a]:
                                    res[index_a].append(p)
        others = 0
        for _, v in actions.items():
            if v == 0:
                others += 1
        print(len(res)+others)


yjsl = YiJianSanLian()
c = int(input().strip())
for i in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    yjsl.calc(n, m)
