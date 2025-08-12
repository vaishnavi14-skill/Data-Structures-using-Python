class Node:
    def __init__(self,coeff,pow):
        self.coeff=coeff
        self.pow=pow
        self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
    def append(self,coeff,pow):
        new_node=Node(coeff,pow)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def printPolynomial(self):
        temp=self.head
        result=[ ]
        while temp:
            result.append(f"{temp.coeff} x^{temp.pow}")
            temp = temp.next
        print(' + '.join(result))
    def addPolynomial(self,p1,p2):
       a=p1
       b=p2
       newhead=Node(0,0)
       c=newhead
       while a is not None or b is not None:
           if a is None:
               c.next=b
               break
           elif b is None:
              c.next=a
              break
           elif a.pow==b.pow:
             c.next=Node(a.coeff+b.coeff,a.pow)
             a=a.next
             b=b.next
           elif a.pow>b.pow:
            c.next=Node(a.coeff,a.pow)
            a=a.next
           else:
            c.next=Node(b.coeff,b.pow)
            b=b.next
           c=c.next
       return newhead.next
poly1=Polynomial()
poly1.append(5,3)
poly1.append(4,2)
poly1.append(2,0)
poly2=Polynomial()
poly2.append(5,1)
poly2.append(5,0)
print("First Polynomial:")
poly1.printPolynomial()
print("Second Polynomial:")
poly2.printPolynomial()
result=Polynomial()
result.head=result.addPolynomial(poly1.head,poly2.head)
print("Resultant Polynomial:")
result.printPolynomial()


                                                                                      
