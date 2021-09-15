import collections


class Solution:
    """
    全国新冠疫苗接种剂次超9亿
    国家卫健委:全国新冠疫苗接种超8亿剂次
    超9亿剂次！1分钟看疫苗接种“中国速度”
    新冠病毒疫苗第二剂次接种“宁迟勿早”
    全国新冠疫苗接种剂次超7亿
    全国新冠疫苗接种超5亿剂次
    广东新冠病毒疫苗接种突破4000万剂次 稳居全国第一
    [新闻直播间]国家卫健委 全国各地累计接种新冠疫苗超9亿剂次
    （一起苗苗苗） 长沙新冠病毒疫苗接种突破300万剂次
    全国累计报告接种新冠疫苗超3.80亿剂次
    超3亿剂次！全国新冠疫苗接种加速推进谁在努力
    """

    def Func(self, query, items):
        count = collections.OrderedDict()
        query = set(list(query))
        for item in items:
            for i in item:
                if i in query:
                    if item in count:
                        count[item] += 1
                    else:
                        count[item] = 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(count[i][0])


if __name__ == "__main__":
    query = input().strip()
    items = []
    while True:
        try:
            item = input().strip()
            items.append(item)
        except EOFError:
            break
    s = Solution()
    s.Func(query, items)
