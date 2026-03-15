from typing import Optional

class ListNode:
    """
    Определение для односвязного списка.
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Объединяет два отсортированных связанных списка в один отсортированный связанный список.

        Args:
            list1: Голова первого отсортированного связанного списка.
            list2: Голова второго отсортированного связанного списка.

        Returns:
            Голова объединенного отсортированного связанного списка.
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
