/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
      
        if(list1 == NULL) return list2;
        if(list2 == NULL) return list1;
        struct ListNode* mlist = list1;
        if(list2->val < list1->val){
            mlist = list2;
            list2 = list2->next;
        }
        else
        {
            list1 = list1->next;
        }
        struct ListNode* temp = mlist;
        while(list1 != NULL && list2 != NULL) 
        {   if(list2->val < list1->val){
                mlist->next = list2;
                list2 = list2->next;
            }
            else {
                mlist->next = list1;
                list1 = list1->next;
            }
            mlist = mlist->next;
        }
        if(!list1)
            mlist->next = list2;
        else 
            mlist->next = list1;

        return temp;

    }
};
