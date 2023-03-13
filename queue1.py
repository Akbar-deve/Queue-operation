# Queue data structure is linear data structure, It follows the principle of "FIFO"(First in First out).
# Insertion of element is happens at rear end & Deletion of element is happens at front end.
# We are creating Queue with the help of List in python.
# Operations can be performed on stack are 
# 1.enqueue()
# 2.dequeue()
# 3.PEEK()
# 4.ISEMPTY()
# 5.DISPLAY()

#creating a class called queue.
class queue:
    def __init__(self):
        #creating queue with the help of list.
        self.data=[]
    
    #Checking whether the Queue is full or not.
    def isEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False
        
    #Function to Display the elements of Queue.
    def display(self):
        print(self.data)
    
    #Function to add the element to the Queue at last.
    def enqueue(self,ele):
        self.data.append(ele)

    #Function to removing element from Queue from front end.
    def dequeue(self):
        if self.isEmpty():
            print('no ele to remove')
        else:
            print(self.data.pop(0))

    #Function displaying the peek element that is top most element of Queue.
    def peek(self):
        if self.isEmpty():
            print('Queue has no ele')
        else:
            print(self.data.pop(0))

#Creating object of class queue.
q=queue()

#while loop for continues execution that is like it execute infinite times
while True:
    print('Select option from below-> ')
    print("1.enqueue\n2.dequeue\n3.display\n4.IsEmpty\n5.Peek")
    opt=int(input("Enter the option to perform "))
    match opt:
        case 1:
            val=int(input('enter the val to insert '))
            q.enqueue(val)
        case 2:
            q.dequeue()
        case 3:
            q.display()
        case 4:
            print("queue has no ele ",q.isEmpty())
        case 5:
            q.peek()
        #If none case is true then the default case _ block will executes.
        case _:
            print(" enter the correct option")


