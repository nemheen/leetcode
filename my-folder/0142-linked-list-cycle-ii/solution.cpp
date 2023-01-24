/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast=head;
        ListNode *slow=head;
        if(!head ||!head->next) return NULL;
        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast){
            ListNode* temp = head;
                while(slow != temp) {
                    slow = slow -> next;
                    temp = temp -> next;
                }
                return temp;
            }
        }
        return NULL;
    }
};
