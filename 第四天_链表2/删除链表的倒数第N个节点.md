# 删除链表的倒数第N个节点
力扣第19题
## 首先的思路,

问题的关键在于说怎么找到“倒数第N个"

那么首先的思路就是说，扫两遍，第一遍统计一下大小，第二遍我去根据大小扫到第N个就行

停下思考一下，如果有10个，那么倒数第二个就是第九个，那么就是10-2+1

但其实链表如果是下标从0开始，那其实就是10-2，但其实在一个for循环中，range(10-2)只能到7，cur从0开始往后走只能走7个，所以rang里面填的其实还是10-2+1
        
但是再其实，我要找的是要删除的前一个，所以最终还是10-2，只不过找到的是前一个而已

不对，range（10-2）虽然只能到7，但其实还是走了8次，但我只想让他走7次，所以是range（10-2-1）

这里应该还要再判断一下删除的是不是size


```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur!=None:
            size += 1
            cur = cur.next
        if n == size:
            return head.next
        cur = head
        for i in range(size-n-1):
            cur = cur.next
        
        cur.next = cur.next.next if cur.next.next else None
        return head
```

## 扫一遍

题目的挑战问了，如何只扫一遍。问题转化为，只扫一遍怎么找到倒数第N个呢

如果先把链表反转过来，再扫，但反转过程已经扫了一遍了，因为还要到倒数第n个，所以还要再扫

偷偷看了一眼答案，very的巧妙的双指针，如果要找倒数第n个，那么思路是弄两个指针，fast先走n步，然后fast和slow一起走，直到fast走到None，然后顺势删除slow就行

那么这里依旧需要思考一下，假设链表长度是size，从左往右链表是0到size-1，倒数第n个即是正着数size-n。循环判定的应该是当fast走到最后的None（即所谓的第size处，那么slow需要走到size-n，或者方便起见，走到size-n-1处，以便删除。
所以二者一个是size，一个是size-n-1，

那么最开始的时候，slow在0处，fast应该在n+1处，这时两个再一起动

fast 在range(n+1)是移动了n次，从0位置移动了n次只能到n，所以需要n+2

其实也可以相差n，即让fast移动到最后一个size-1就行.这样最开始range就是n+1

啊不对不对，狠狠的纠正一下，range(n)其实是走了n步，所以直接走n步就行

不用虚拟节点
```python 
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow,fast = head,head
    for i in range(n):
        fast = fast.next
    if fast == None:#说明正好要删除头节点，直接返回headnext
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

```




