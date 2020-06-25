A1 = int(input())  # Box 1
B1 = int(input())
C1 = int(input())
A2 = int(input())  # Box 2
B2 = int(input())
C2 = int(input())
if ((A1 == A2 and B1 == B2 and C1 == C2) or
        (A1 == A2 and B1 == C2 and C1 == B2) or
        (A1 == C2 and B1 == A2 and C1 == B2) or
        (A1 == B2 and B1 == A2 and C1 == C2) or
        (A1 == B2 and B1 == C2 and C1 == A2) or
        (A1 == C2 and B1 == B2 and C1 == A2)):
    print('Boxes are equal')
elif ((A1 <= A2 and B1 <= B2 and C1 <= C2) or
      (A1 <= A2 and B1 <= C2 and C1 <= B2) or
      (A1 <= C2 and B1 <= A2 and C1 <= B2) or
      (A1 <= B2 and B1 <= A2 and C1 <= C2) or
      (A1 <= B2 and B1 <= C2 and C1 <= A2) or
      (A1 <= C2 and B1 <= B2 and C1 <= A2)):
    print('The first box is smaller than the second one')
elif ((A1 >= A2 and B1 >= B2 and C1 >= C2) or
      (A1 >= A2 and B1 >= C2 and C1 >= B2) or
      (A1 >= C2 and B1 >= A2 and C1 >= B2) or
      (A1 >= B2 and B1 >= A2 and C1 >= C2) or
      (A1 >= B2 and B1 >= C2 and C1 >= A2) or
      (A1 >= C2 and B1 >= B2 and C1 >= A2)):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
