#none
a=None
print(a)
print(type(a))
print('-'*80)

#numeric types
#int
x=4+3j
print(type(x))

#sequence type
#list(
#1.ordered collection of elements)
#2.created using within sqaure brackets
#3.it is mutable
#4.it allows duplicates
#print[1,2,2,1,3,3]
#5.it allows both homogeneous and heterogeneous elements
#x=[1,2.2,true,'abc']

x=[]
print(type(x))
# from last negative value like -1,-2,-3,-4,-5
x=[10,20,30,40,50]
print(x[0])
print(x[-3])
#it stops at 2nd index...3 index is discarded(start,stop,step)
print(x[0:3:1])
print(x[::4])
print(x[2:3:4])
#start<stop step=+ve value
#stop<start step=-ve value
print(x[4::-1])


l=[10,20,30]
l=l+[40]
print(l)
l.append(40)
print(l)


l.extend([50,60,70])
print(l)
l.insert(2,[50,60,70])
print(l)


t=10,20,30
print(type(t))

a,b,c=t
print(a)
print(b)
print(c)



sentence = "a quick brown fox"
part1 = sentence[2:7] 
part2 = sentence[-3::]
part3 = sentence[2:7:2]
part4 = sentence[-2:-4:-4]
part5 = sentence[15:13:-1]
part6 = sentence[12:1:-2]
print(part1)  
print(part2)  
print(part3)  
print(part4) 
print(part5)  
print(part6)

s={1,2,3,4,5,6,1}
print(len(s))
print(type(s))

student={'name':'ravi','phone':123456,'email':'netra@123'}
print(student)