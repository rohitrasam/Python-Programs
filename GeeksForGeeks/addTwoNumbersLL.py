# Given two decimal numbers represented by two linked lists of size N and M respectively. The task is to return a linked list that represents the sum of these two numbers.

# For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null. You are required to return the head of the linked list 2->1->5->null.

# Example 1:

# Input:
# N = 2
# valueN[] = {4,5}
# M = 3
# valueM[] = {3,4,5}
# Output: 3 9 0  
# Explanation: For the given two linked
# list (4 5) and (3 4 5), after adding
# the two linked list resultant linked
# list will be (3 9 0).
# Example 2:

# Input:
# N = 2
# valueN[] = {6,3}
# M = 1
# valueM[] = {7}
# Output: 7 0
# Explanation: For the given two linked
# list (6 3) and (7), after adding the
# two linked list resultant linked list
# will be (7 0).


#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def reverse(head):
    prev = None
    curr = head
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here

        first = reverse(first)
        second = reverse(second)
        sum = None
        carry = 0

        while first is not None or second is not None or carry != 0:

            newVal = carry
            if first:
                newVal += first.data
            if second:
                newVal += second.data
            
            carry = newVal // 10
            newVal = newVal % 10
            newNode = Node(newVal)
            newNode.next = sum
            sum = newNode

            if first:
                first = first.next
            if second:
                second = second.next
        
        return sum
        # return head of sum list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends