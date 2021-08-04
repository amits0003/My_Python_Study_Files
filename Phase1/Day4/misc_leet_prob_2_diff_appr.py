
from builtins import  *
class Solution:
    'hello'
    def addTwoNumbers(self, l1 : ListNode , l2 : ListNode ,carry = 0) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value = l1.val + l2.val + carry
        carry = value // 10
        res_value = ListNode(value % 10 ) 
        
        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            res_value.next = self.addTwoNumbers(l1.next,l2.next,carry)
        return res_value
    
    listA = [2,4,3]
    listB = [5,6,4]
    
    print(addTwoNumbers(listA, listB))