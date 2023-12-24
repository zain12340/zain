# list=[5,7,1]
# mult=1
# for x in list:
#  mult*=x 
# print(mult) 


# list=[5,7,1,4,8]
# list1=[]  

# for x in list:
   
#    if(x%2!=0): 
#     list1.append(x)

     
# print(list1)



def sym(s1):
    l=s1
    y=0

    y=len(l)//2
    h=l[:y]
    p=l[y:]

    if h==p:
       print("semtrkl")

sym("menmen")
sym("movemove")
