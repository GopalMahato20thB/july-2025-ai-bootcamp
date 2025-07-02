class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # the number in the node
        self.next = next    # pointer to next node

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Step 1: Create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy  # This will help us build the result list step-by-step

        # Step 2: While both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1      # link smaller node to result
                list1 = list1.next     # move in list1
            else:
                tail.next = list2      # link smaller node to result
                list2 = list2.next     # move in list2
            tail = tail.next           # move tail forward

        # Step 3: Attach the remaining nodes
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # Step 4: Return merged list (skip dummy node)
        return dummy.next

