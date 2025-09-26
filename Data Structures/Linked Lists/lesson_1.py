# create a class for node to be used for the linked list
class Node:
    def __init__(self, value):  # initialization function
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # to print an entire list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # append item to end

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):  # edge cases: only one node exists or is None
        if self.length == 0:  # edge case where there is none
            return None
        temp = self.head
        pre = self.head
        while temp.next:  # as long as temp.next is not None
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:  # edge case where one node exists after length reduction
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):  # underscore used as no variable is passed in the for loop
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        prev = self.get(index - 1)
        temp = prev.next  # this is the more efficient way since get is O(n)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # reverse linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        #   ninjas have good brains out here...>Watch this<
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        #     while implementation
        # while temp is not None:
        #     after = temp.next
        #     temp.next = before
        #     before = temp
        #     temp = after


# my_linkedlist = LinkedList(5)
# my_linkedlist.append(3)
# my_linkedlist.prepend(7)
# my_linkedlist.print_list() 

# Insert test
# my_linkedlist = LinkedList(0)
# my_linkedlist.append(3)
# my_linkedlist.insert(1, 2)
# my_linkedlist.print_list()

# # set_value  and remove test
# my_linkedlist = LinkedList(11)
# my_linkedlist.append(4)
# my_linkedlist.append(2)
# my_linkedlist.append(8)

# my_linkedlist.set_value_1(2,5)
# print(my_linkedlist.remove(2), '\n')
# my_linkedlist.print_list()

# # get and reverse test
my_linkedlist = LinkedList(0)
my_linkedlist.append(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
# print(my_linkedlist.get(2))
print("Before reversal: ")
my_linkedlist.print_list()
my_linkedlist.reverse()
print("\n After reversal: ")
my_linkedlist.print_list()

# # Pop test
# # (2) items - Returns 2 Nodes
# print(my_linkedlist.pop().value)
# # (1) items - Returns 1 Node
# print(my_linkedlist.pop().value)
# # (0) items - Returns None
# print(my_linkedlist.pop())

# # Pop_first test 
# # (2) items - Returns 2 Nodes
# print(my_linkedlist.pop_first().value)
# # (1) items - Returns 1 Node
# print(my_linkedlist.pop_first().value)
# # (0) items - Returns None
# print(my_linkedlist.pop_first())

# first value seems to disappear, error was caused by using new_value in append stage instead of new_node

# test of long method for set_value
# def set_value_1(self, index, value):
#     if index < 0  or index >= self.length:
#         return None
#     temp = self.head
#     for _ in range(index): #underscore used as no variable is passed in the for loop
#         temp = temp.next
#         temp.value = value
#     return temp
