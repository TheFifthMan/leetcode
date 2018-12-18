# coding: utf-8
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
#=================================================================

'''
遍历每个元素 xx，并查找是否存在一个值与 target - xtarget−x 相等的目标元素。
执行时间：6976 ms	
'''
def two_num_1(target,nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if target - nums[i] == nums[j]:
                return [i,j]
        

'''
两遍哈希表
执行时间48ms
'''
def two_num_2(target,nums):
    record =  {}
    for num in range(0,len(nums)):
        record[nums[num]] = num
    
    for num in range(0,len(nums)):
        value = target - nums[num]
        if value in record.keys() and record.get(value)!=num:
            return [num,record.get(value)]

'''
一遍哈希表
执行耗时 48ms
'''
def two_num_3(target,nums):
    record = {}
    for num in range(0,len(nums)):
        value = target - nums[num]
        if value in record.keys():
            # 立马返回之前已经存储的数据和当前符合情况的索引
            return [record.get(value),num]
        # 否则继续替换值
        record[nums[num]] = num
        
# 执行时间1020ms
def two_num_myself(target,nums):
    for num in range(0,len(nums)):
        value = target - nums[num]
        try:
            p2 = nums.index(value,num+1)
            if value in nums:
                return [num,p2]
        except:
            pass
            

if __name__ == "__main__":
    nums = [0,1,3,4,5]
    target = 16021
    
    print(two_num(target,nums))