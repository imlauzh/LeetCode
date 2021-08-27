class Solution:
    def func(self, inputs):
        print(inputs)


# int 无限行
# 1
# 2
s = Solution()
inputs=[]
while True:
    try:
        inp = input().strip()
        if inp:
            inputs.append(inp)
    except EOFError:
        break
res = s.func(inputs)
print(res)


# # int
# # 1
# s = Solution()
# inputs = input().strip()
# inputs = int(inputs)
# res = s.func(inputs)
# print(res)


# # int list
# # [1,2,3]
# s = Solution()
# inputs = input().strip()
# input_list = list(map(int, inputs.split(']')[0].split('[')[-1].split(',')))
# res = s.func(input_list)
# print(res)


# # 2 int list
# # [4,5,6],[1,2,3]
# s = Solution()
# inputs = input().strip()
# inputs=inputs.split('],[')
# input_list1 = list(map(int, inputs[0].strip('[').split(',')))
# input_list2= list(map(int, inputs[1].strip(']').split(',')))
# res = s.func([input_list1,input_list2])
# print(res)


# # 2d int list, int
# # [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
# s = Solution()
# inputs = input().strip()
# inputs = inputs.split(']],')
# k = int(inputs[1])
# matrix = list(list(map(int,i.split(','))) for i in inputs[0].strip('[[').split('],['))
# res = s.func(matrix)
# print(res)


# # float list
# # [1.0, 2.0, 3.0]
# s = Solution()
# inputs = input().strip()
# input_list = list(map(float, inputs.split(']')[0].split('[')[-1].split(',')))
# res = s.func(input_list)
# print(res)

# # int list + int
# # [1,2,3], 3
# s = Solution()
# inputs = input().strip()
# inputs=inputs.split('],')
# target = int(inputs[-1])
# input_list = list(map(int, inputs[0].strip('[').split(',')))
# print(target)
# res = s.func(input_list)
# print(res)


# # list node + int
# # {1,2,3}, 3
# s = Solution()
# inputs = input().strip()
# inputs=inputs.split('},')
# target = int(inputs[-1])
# input_list = list(map(int, inputs[0].strip('{').split(',')))
# print(target)
# res = s.func(input_list)
# print(res)


# # str
# # "abcd"
# s = Solution()
# inputs = input().strip()
# inputs=str(inputs.strip('"'))
# res = s.func(inputs)
# print(res)


# # str, int
# # "abc1234321ab",12
# s = Solution()
# inputs = input().strip()
# inputs=inputs.split('",')
# length=int(inputs[1])
# inputs=str(inputs[0].strip('"'))
# res = s.func([inputs,length])
# print(res)


# # str list
# # ["PSH1","PSH2","POP","POP"]
# s = Solution()
# inputs = input().strip()
# inputs=inputs.strip('["').strip('"]')
# input_list = list(map(str, inputs.split('","')))
# res = s.func(input_list)
# print(res)
