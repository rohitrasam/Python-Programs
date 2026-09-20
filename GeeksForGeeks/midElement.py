# Given a singly linked list of N nodes.
# The task is to find the middle of the linked list. For example, if the linked list is
# 1-> 2->3->4->5, then the middle node of the list is 3.
# If there are two middle nodes(in case, when N is even), print the second middle element.
# For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

# Example 1:

# Input:
# LinkedList: 1->2->3->4->5
# Output: 3 
# Explanation: 
# Middle of linked list is 3.
# Example 2: 

# Input:
# LinkedList: 2->4->6->7->5->1
# Output: 7 
# Explanation: 
# Middle of linked list is 7.


# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        size = 1
        
        curr = head
        
        while curr.next:
            curr = curr.next
            size += 1
            
        curr = head
        size //= 2
        for i in range(size):
            curr = curr.next
        
        return curr.data
            
        



#{ 
 # Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))


# } Driver Code Ends