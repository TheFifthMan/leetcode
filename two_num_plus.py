# coding: utf-8 
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

测试用例：
[2,4,5] + [5,6,4] = [7,0,8]

'''
# Definition for singly-linked list.

#class ListNode:
#    def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # head 指向的是一个对象，在电脑中，表示为一个地址
        head = ListNode(0)
        # 将这个地址 赋值给 一个叫做curr 的变量，让curr 去添加链条
        curr = head
        p,q = l1,l2
        carry= 0
        while p!=None or q!=None:
            if p!=None: 
                x=p.val 
            else:
                x=0
            if q!=None: 
                y=q.val
            else: 
                y=0
            sum = carry + x + y
            carry = 0
            if sum >= 10:
                carry = 1
                
            next_num = sum % 10
            curr.next = ListNode(next_num)
            curr = curr.next 
            if p!=None: p = p.next
            if q!=None: q = q.next
            
                
        if carry > 0:
            curr.next = ListNode(carry)
        
        # 经过一番操作以后，curr 现在已经不知道指向链条上面的哪一个点了，但是head还是head
        return head.next

        

if __name__ == "__main__":
    pass