class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL) return list2;
        if(list2 == NULL) return list1;
        
        ListNode * mlist = list1;
        if(list1 -> val > list2 -> val)
        {
            mlist = list2;
            list2 = list2 -> next;
        }
        else
        {
            list1 = list1 -> next;
        }
        ListNode *temp = mlist;

        while(list1 &&  list2)
        {
            if(list1 -> val < list2 -> val){
                temp->next = list1;
                list1 = list1 -> next;
            }
            else{
                temp->next = list2;
                list2 = list2 -> next;
            }
            temp = temp -> next;        
        }
		
        if(!list1)
            temp -> next = list2;
        else
            temp -> next = list1;
            
        return mlist;
    }
};
