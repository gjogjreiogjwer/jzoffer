def FindKthToTail(head, k):
    list=[]
    while head:
        list.append(head)
        head=head.next
    length=len(list)
    if k>length or k<1:
        return None
    return list[-k]


    
