class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_list = ListNode(0, None)
        head = None

        if list1.val < list2.val:
            head = ListNode(list1.val, None)
        else:
            head = ListNode(list2.val, None)

        while list1 is not None and list2 is not None:
            cur_list.next = ListNode(0, None)

            if list1.val < list2.val:
                cur_list.val = list1.val
                list1 = list1.next
            else:
                cur_list.val = list2.val
                list2 = list2.next

            cur_list = cur_list.next

        if list1 is not None:
            cur_list.next = ListNode(list1.val, None)
        else:
            cur_list.next = ListNode(list2.val, None)

        return head

