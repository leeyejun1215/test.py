A = (input("몇 단까지 출력할까요?"))
a = int(A)
for B in range(1, a+1) :
    print("----[",B,"단]----")
    for b in range(1,B+1) :
      print(B,"x",b,"=",B*a)