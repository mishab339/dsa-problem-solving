class ListNode{
    constructor(val,next=null){
        this.val = val;
        this.next = next;
    }
}
var mergeTwoList = function(list1,list2){
    let dummy = new ListNode();
    let curr = dummy;
    while(list1&&list2){
        if(list1.val>list2.val){
         curr.next = list2;
         list2 = list2.next;
        }else{
            curr.next = list1;
            list1 = list1.next
        }
        curr = curr.next;
    }
    curr.next = list1||list2;
    console.log(curr.next);
    return dummy.next;
}
const list1 = new ListNode(1,new ListNode(3,new ListNode(5)));
const list2 = new ListNode(3,new ListNode(4,new ListNode(6)));
console.log(mergeTwoList(JSON.stringify(mergeTwoList(list1,list2))));

