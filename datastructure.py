#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  ARRAYS  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
An array is collection of items stored at contiguous memory locations. 
The idea is to store multiple items of same type together. 
This makes it easier to calculate the position of each element by simply adding an offset to a base value, 
i.e., the memory location of the first element of the array (generally denoted by the name of the array)

Advantages of using arrays:

Arrays allow random access of elements. This makes accessing elements by position faster.
Arrays have better cache locality that can make a pretty big difference in performance.



from array import *
array1 = array('i', [10,20,30,40,50])

for x in array1:
    print(x)


# left rotation of an array
def leftrotate(arr,d,n):
    for j in range(d):
        new_node=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=new_node

def printarr(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
arr=[1,2,3,4,5]
n=5
d=2
leftrotate(arr,d,n)
printarr(arr,n)



# DYNAMIC ARRAY
What is a dynamic array?

A dynamic array is similar to an array, but with the difference that its size can be dynamically modified at runtime. 
Don’t need to specify how much large an array beforehand. 
The elements of an array occupy a contiguous block of memory, and once created, its size cannot be changed. 
A dynamic array can, once the array is filled, allocate a bigger chunk of memory, copy the contents from the original array to this new space, 
and continue to fill the available slots










#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LINKED LIST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

dynamic data structure made of nodes
data is not stored in continuous manner
insertion and deletion of elements is easier
can be used to implement abstract data types like stack , queue , list
efficient random access is not possible
implementation recquires some extra memory

types:- 
single linked list
double linked list
circular linked list
linked list with header node
sorted linked list

# SINGLE  LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            


    def insert_at_after (self,data,x):
        new_node=Node(data)
        temp=self.head
        while temp.data is not x:
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def insert_at_before (self,data,x):
        new_node=Node(data)
        temp=self.head
        if temp.data is x:
            new_node.next=temp
            temp=new_node
            return
        else:
            while temp.next.data is not x:
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node


    def createList(self):
        n=int(input("Enter the no. of elements in the linkedlist : "))
        if n==0:
            print("list is empty")
        else:
            for i in range(n):
                data=int(input("enter the elements to be inserted : "))
                self.insert_at_end(data)

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
llist=LinkedList()
llist.createList()
# llist.insert_at_after(100,2)
llist.insert_at_before(20,1)
llist.printList()
 
        





class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedList:

    def __init__(self):
        self.head=None

    def display_list(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            print("List is :  ")
            temp=self.head
            while temp is not None:
                print(temp.value," ", end =' ')
                temp=temp.next
            print()
                
    
    def count_node(self):
        temp=self.head
        n=0
        if temp is None:
            print("the no of node is - ",n)
        else:
            while temp is not None:
                n=n+1
                temp=temp.next
            print("the no of nodes are: ",n)

    def search(self,x):
        position=1
        temp=self.head
        if temp is None:
            print("Not found because list is empty")
        else:
            while temp is not None:
                if temp.value==x:
                    print("element found at position : ",position)
                    break
                else:
                    temp=temp.next
                    position=position+1

        
    
    def insert_in_beginning(self,data):             #it also work if the list is empty
        new_node=Node(data)                             #new_node=Node(data)
        new_node.next=self.head                        #new_node.next=None
        self.head=new_node                             #self.head=new_node

        

    def insert_at_end(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node



    def create_list(self):
        n=int(input("enter the no of nodes : "))
        if n==0:
            return
        else:
            for i in range(n):
                data=int(input("enter the elements to be inserted : "))
                self.insert_at_end(data)




    def insert_after(self,data,x):
        temp=self.head
        while temp is not None:
            if temp.value==x:
                break
            temp=temp.next
        if temp is None:
            print(x," is not present in the list ")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node
        


    def insert_before(self,data,x):
        temp=self.head
        #if list is empty
        if temp is None:
            print(x," is not present because list is empty")
            return

        #if insertion is done before first node
        if x==temp.value:
            new_node=Node(data)
            new_node.next=temp
            temp=new_node
            return
        
        #find reference to redecesor of node containing x
        while temp.next is not None:
            if temp.next.value==x:
                break
            temp=temp.next
        if temp.next is None:
            print(x," not present in the list")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node


    
    def insert_at_position(self,data,x):
        if k==1:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        i=1
        while i<k-1 and temp is not None:
            temp=temp.next
            i+=1
        if temp is None:
            print("you can insert only upto",i)
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node

    
    def delete_node(self,x):
        if self.head is None:
            print("list is empty")
            return
        #deletion of first node
        if self.head.value==x:
            self.head=self.head.next
            return
        #deletion in between or end
        temp=self.head
        while temp.next is not None:
            if temp.next.value==x:
                break
            temp=temp.next
        if temp.next is None:
            print("element", x , "not in the list")
        else:
            temp.next=temp.next.next



        

    def delete_first_node(self):
        if self.head is None:
            return
        self.head=self.head.next


    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None


    def reverse_list(self):
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 


    def bubble_sort_exdata(self):
        i=0
        while i< len(list1):
            j=0
            while j<i:
                if list1[i]<list1[j]:
                    #swap operation
                    new_node=list1[j]
                    list1[i]=list1[j]
                    list1[j]=new_node
                j=j+1
            i=i+1

    def bubble_sort_elinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self,x):
        pass

    def merge2(self,list2):
        pass
    def _merge2(self,p1,p2):
        pass

    def merge_sort(self):
        pass
    def _merge_sort_rec(self,listhead):
        pass
    
    def _divide_list(self,temp):
        pass




list1 =SingleLinkedList()
list1.create_list()

while True:
    print("1. Display the list")
    print("2. count no of nodes")
    print("3. search for an element")
    print("4. insert in emptylist/insert at the beginning of the list")
    print("5. insert a node at the end of the list")
    print("6. insert a node after a speified node")
    print("7. insert a node before a specified node")
    print("8. insert a node at a given position")
    print("9. delete the first node")
    print("10. delete last node")
    print("11. delete any node")
    print("12. reverse the list")
    print("13. bubble sort by exchanging data")
    print("14. bubble sort by exchanging lists")
    print("15. mergesort")
    print("16. insert cycle")
    print("17. detect cycle")
    print("18. remove cycle")
    print("19. quit")

    option =int(input("enter your option :  "))

    if option ==1:
        list1.display_list()
    elif option==2:
        list1.count_node()
    elif option==3:
        data = int(input("enter the element to be searched : "))
        list1.search(data)
    elif option==4:
        data=int(input("enter the elements to be inserted : "))
        list1.insert_in_beginning(data)
    elif option ==5:
        data=int(input("enter the elements to be inserted : "))
        list1.insert_at_end(data)
    elif option==6:
        data=int(input("enter the elements to be inserted : "))
        x=int(input("enter the elements after which to be inserted : "))
        list1.insert_after(data,x)
    elif option ==7:
        data=int(input("enter the elements to be inserted : "))
        x=int(input("enter the elements before which to be inserted : "))
        list1.insert_before(data,x)
    elif option==8:
        data=int(input("enter the elements to be inserted : "))
        k=int(input("enter the position at which to be inserted : "))
        list1.insert_at_position(data,k)
    elif option==9:
        list1.delete_first_node()
    elif option==10:
        list1.delete_last_node()
    elif option==11:
        data=int(input("enter the elements to be deleted : "))
        list1.delete_node(data)
    elif option==12:
        list1.reverse_list()
    elif option==13:
        list1.bubble_sort_exdata()
    elif option==14:
        list1.bubble_sort_elinks()
    elif option==15:
        list1.merge_sort()
    elif option==16:
        data=int(input("enter the elements at which cycle has  to be inserted : "))
        list1.insert_cycle(data)
    elif option==17:
        if list1.has_cycle():
            print("list has a cycle")
        else:
            print("list does not have a cycle ")
    elif option==18:
        list1.remove_cycle()
    elif option==19:
        break
    else:
        print("wrong option")
    print()

    
        


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DOUBLE LINKED LIST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
in this list and every node with one another in both direction so the traversal can be done from head to tail or vice versa
pointer head points first/head node
previous part of first node and next part of last node will always be null
next part of each  node contain address of succeror node
previous part of each node contains address of predecessor node


class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        # temp=self.head     here it does not print the result if we use temp
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        new_node.next=None
        # temp=self.head       here it does not print the result if we use temp
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        return
    def delete_node(self):
        pass



    def createList(self):
        n=int(input("Enter the no. of elements present in the list : "))
        for i in range(n):
            data=int (input(f"Enter the {i}st element : "))
            self.insert_at_end(data)


    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next

llist=DoubleLinkedList()
llist.createList()
llist.insert_at_beginning(50)
llist.insert_at_end(100)
llist.printList()









#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CIRCULAR LINKED LIST  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Why have we taken a pointer that points to the last node instead of first node ?
For insertion of node in the beginning we need traverse the whole list.
Also, for insertion and the end, the whole list has to be traversed.
If instead of head pointer we take a pointer to the last node then in both the cases there won’t be any need to traverse the whole list. 
So insertion in the begging or at the end takes constant time irrespective of the length of the list.


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLinkedList():
    def __init__(self):
        self.last=None
    

    def insert_at_empty(self,data):
        newnode=Node(data)
        if self.last is None:
            self.last=newnode
            newnode.next=newnode

    def insert_at_beginning(self,data):
        newnode=Node(data)
        if self.last is None:
            self.last=newnode
            newnode.next=newnode
        else:
            newnode.next=self.last.next
            self.last.next = newnode

    
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.last is None:
            self.last=newnode
            newnode.next=newnode
        else:
            newnode.next=self.last.next
            self.last.next=newnode
            self.last=newnode

    def insert_in_between(self,data,item):
        if self.last is None:
            return None
        newnode=Node(data)
        temp=self.last.next
        while temp:
            if (temp.data == item): 
                newnode.next = temp.next
                temp.next = newnode 
  
                if (temp == self.last): 
                    self.last = newnode
                    return self.last 
                else: 
                    return self.last 
            temp = temp.next
            if (temp == self.last.next): 
                print(item, "not present in the list") 
                break



    def printlist(self):

        if (self.last == None): 
            print("List is empty") 
            return
        new_node=self.last.next
        while new_node is not None :
            print(new_node.data,end=" ")
            new_node=new_node.next
            if new_node== self.last.next:
                break
  

if __name__ == "__main__":

    llist=CircularLinkedList()
    llist.insert_at_empty(55)
    llist.insert_at_beginning(99)
    llist.insert_at_beginning(109)
    llist.insert_at_end(39)
    llist.insert_at_end(40)
    llist.insert_in_between(67,99)
    llist.printlist()
            
            


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  STACK  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Stack is a linear data structure which follows a particular order in which the operations are performed.
The order may be LIFO(Last In First Out) or FILO(First In Last Out).

Stack can be implemented using [ LIST, QUEUE, LIQUEUE]


Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, 
then it is said to be an Underflow condition.

Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else false.


# Python program to 
# demonstrate stack implementation 
# using list 


stack = [] 

# append() function to push 
# element in the stack 
stack.append('a') 
stack.append('b') 
stack.append('c') 

print('Initial stack') 
print(stack) 

# pop() fucntion to pop 
# element from stack in 
# LIFO order 
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print('\nStack after elements are poped:') 
print(stack) 

# uncommenting print(stack.pop()) 
# will cause an IndexError 
# as the stack is now empty 




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  QUEUE  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
A Queue is a linear structure which follows a particular order in which the operations are performed. 
The order is First In First Out (FIFO). 
A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 
The difference between stacks and queues is in removing. 
In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

Queue can also be implemented using [ LIST,QUEUE,LIQUEUE]

# PRIORITY QUEUE
Priority Queue is an extension of queue with following properties.

Every item has a priority associated with it.
An element with high priority is dequeued before an element with low priority.
If two elements have the same priority, they are served according to their order in the queue.


Heap data structure is mainly used to represent a priority queue. In Python, it is available using “heapq” module. 
The property of this data structure in python is that each time the smallest of heap element is popped(min heap). 
Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.
Operations on heap :

1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.

2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. 
The order is adjusted, so as heap structure is maintained.

3. heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained
4. heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. 
Heap order is maintained after this operation.

5. heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. 
In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. 
heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop()
 nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.

7. nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned

# Python code to demonstrate working of 
# heappushpop() and heapreplce() 

# importing "heapq" to implement heap queue 
import heapq 

# initializing list 1 
li1 = [5, 7, 9, 4, 3] 

# initializing list 2 
li2 = [5, 7, 9, 4, 3] 

# using heapify() to convert list into heap 
heapq.heapify(li1) 
heapq.heapify(li2) 

# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappushpop(li1, 2)) 

# using heapreplace() to push and pop items simultaneously 
# pops 3 
print ("The popped item using heapreplace() is : ",end="") 
print (heapq.heapreplace(li2, 2)) 


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  DEQUEUE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

# Python code to demonstrate working of 
# append(), appendleft(), pop(), and popleft() 

# importing "collections" for deque operations 
import collections 

# initializing deque 
de = collections.deque([1,2,3]) 

# using append() to insert element at right end 
# inserts 4 at the end of deque 
de.append(4) 

# printing modified deque 
print ("The deque after appending at right is : ") 
print (de) 

# using appendleft() to insert element at right end 
# inserts 6 at the beginning of deque 
de.appendleft(6) 

# printing modified deque 
print ("The deque after appending at left is : ") 
print (de) 

# using pop() to delete element from right end 
# deletes 4 from the right end of deque 
de.pop() 

# printing modified deque 
print ("The deque after deleting from right is : ") 
print (de) 

# using popleft() to delete element from left end 
# deletes 6 from the left end of deque 
de.popleft() 

# printing modified deque 
print ("The deque after deleting from left is : ") 
print (de) 




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CIRCULAR QUEUE  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Circular Queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
and the last position is connected back to the first position to make a circle. It is also called ‘Ring Buffer’.

class CircularQueue(): 

	# constructor 
	def __init__(self, size): # initializing the class 
		self.size = size 
		
		# initializing queue with none 
		self.queue = [None for i in range(size)] 
		self.front = self.rear = -1

	def enqueue(self, data): 
		
		# condition if queue is full 
		if ((self.rear + 1) % self.size == self.front): 
			print(" Queue is Full\n") 
			
		# condition for empty queue 
		elif (self.front == -1): 
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data 
		else: 
			
			# next position of rear 
			self.rear = (self.rear + 1) % self.size 
			self.queue[self.rear] = data 
			
	def dequeue(self): 
		if (self.front == -1): # codition for empty queue 
			print ("Queue is Empty\n") 
			
		# condition for only one element 
		elif (self.front == self.rear): 
			new_node=self.queue[self.front] 
			self.front = -1
			self.rear = -1
			return new_node 
		else: 
			new_node = self.queue[self.front] 
			self.front = (self.front + 1) % self.size 
			return new_node 

	def display(self): 
	
		# condition for empty queue 
		if(self.front == -1): 
			print ("Queue is Empty") 

		elif (self.rear >= self.front): 
			print("Elements in the circular queue are:", 
											end = " ") 
			for i in range(self.front, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 

		else: 
			print ("Elements in Circular Queue are:", 
										end = " ") 
			for i in range(self.front, self.size): 
				print(self.queue[i], end = " ") 
			for i in range(0, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 

		if ((self.rear + 1) % self.size == self.front): 
			print("Queue is Full") 

# Driver Code 
ob = CircularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.display() 








#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  BINARY TREE  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
A tree whose elements have at most 2 children is called a binary tree. 
Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

A Binary Tree node contains following parts.

Data
Pointer to left child
Pointer to right child



Traversal
Breadth First Search
(1) - Level order (visit all node at same level from top then left of same level and then right )

Depth First Search
(a) Inorder (Left, Root, Right) 
(b) Preorder (Root, Left, Right) 
(c) Postorder (Left, Right, Root)



# Python program to for tree traversals 

# A class that represents an individual node in a 
# Binary Tree 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


# A function to do inorder tree traversal 
def printInorder(root): 

	if root: 

		# First recur on left child 
		printInorder(root.left) 

		# then print the data of node 
		print(root.val),

		# now recur on right child 
		printInorder(root.right) 



# A function to do postorder tree traversal 
def printPostorder(root): 

	if root: 

		# First recur on left child 
		printPostorder(root.left) 

		# the recur on right child 
		printPostorder(root.right) 

		# now print the data of node 
		print(root.val), 


# A function to do preorder tree traversal 
def printPreorder(root): 

	if root: 

		# First print the data of node 
		print(root.val), 

		# Then recur on left child 
		printPreorder(root.left) 

		# Finally recur on right child 
		printPreorder(root.right) 


# Driver code 
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print ("Preorder traversal of binary tree is")
printPreorder(root) 

print ("\nInorder traversal of binary tree is")
printInorder(root) 

print ("\nPostorder traversal of binary tree is")
printPostorder(root) 


# INSERTION IN A BINARY TREE

# Python program to insert element in binary tree 
class newNode(): 

	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None
		
""" Inorder traversal of a binary tree"""
def inorder(new_node): 

	if (not new_node): 
		return

	inorder(new_node.left) 
	print(new_node.key,end = " ") 
	inorder(new_node.right) 


"""function to insert element in binary tree """
def insert(new_node,key): 

	q = [] 
	q.append(new_node) 

	# Do level order traversal until we find 
	# an empty place. 
	while (len(q)): 
		new_node = q[0] 
		q.pop(0) 

		if (not new_node.left): 
			new_node.left = newNode(key) 
			break
		else: 
			q.append(new_node.left) 

		if (not new_node.right): 
			new_node.right = newNode(key) 
			break
		else: 
			q.append(new_node.right) 
	
# Driver code 
if __name__ == '__main__': 
	root = newNode(10) 
	root.left = newNode(11) 
	root.left.left = newNode(7) 
	root.right = newNode(9) 
	root.right.left = newNode(15) 
	root.right.right = newNode(8) 

	print("Inorder traversal before insertion:", end = " ") 
	inorder(root) 

	key = 12
	insert(root, key) 

	print() 
	print("Inorder traversal after insertion:", end = " ") 
	inorder(root) 



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  BINARY SEARCH TREE  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
Elements are always unique in BST 



# A utility function to search a given key in BST 
def search(root,key): 
	
	# Base Cases: root is null or key is present at root 
	if root is None or root.val == key: 
		return root 

	# Key is greater than root's key 
	if root.val < key: 
		return search(root.right,key) 
	
	# Key is smaller than root's key 
	return search(root.left,key) 


