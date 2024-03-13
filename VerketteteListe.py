from collections.abc import Iterator


class Iterator(Iterator):
    def __init__(self,sequence):
        self._sequence = sequence
        self._next = None

    def __next__(self):
        if self._next < len(self._sequence):
            item = self._sequence[self._next]
            self._next+=1
            return item
        else:
            raise StopIteration



class linkedList:
    def __init__(self):
        self.Head = None

    def printList(self):
        current = self.Head
        while current is not None:
            print(current._sequence, end =" ")
            current = current._next

    def insertIntoEmptyList(self,element):
        newElement = Iterator(element)
        self.Head = newElement

    def insertAtEnd(self,element):
        if self.Head is None:
            newElement = Iterator(element)
            self.Head = newElement
        else:
            current = self.Head
            while current._next is not None:
                current = current._next
            newElement = Iterator(element)
            current._next = newElement

    def insertAtBegining(self,element):
        if self.Head is None:
            newElement = Iterator(element)
            self.Head = newElement
        else:
            newElement = Iterator(element)
            newElement._next = self.Head
            self.Head = newElement

    def DeleteElement(self,pos):
        counter = 0
        current = self.Head
        previous = None
        while current._next is not None and counter < pos:
            counter += 1
            previous = current
            current = current._next
        if current == self.Head:
            self.Head = current._next
            del current
        else:
            previous._next = current._next
            del current





    def Length(self):
        counter = 0
        current = self.Head

        while current is not None:
            counter  += 1
            current = current._next
        print("Länge der Datenstruktur: ", counter, end =" ")


MylinkedList = linkedList()

MylinkedList.insertIntoEmptyList(15)
MylinkedList.insertAtEnd(1)
MylinkedList.insertAtEnd(21)
MylinkedList.insertAtEnd(31)
MylinkedList.insertAtEnd(25)

MylinkedList.insertAtBegining(4)
MylinkedList.DeleteElement(2)


MylinkedList.printList()
MylinkedList.Length()