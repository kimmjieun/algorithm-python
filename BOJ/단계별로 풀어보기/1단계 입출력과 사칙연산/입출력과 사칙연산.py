
#2557번 Hello World
print('Hello World!')


#10718번 We love kriii
print('강한친구 대한육군')
print('강한친구 대한육군')

#10171번 고양이
print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

#10172번 개
print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|\"^\"`    |')
print('||_/=\\\\__|')

#1000번 A+B
a, b = map(int,input().split())
print(a+b)

#1001번 A-B
a, b = map(int,input().split())
print(a-b)


#109998번 A×B
a, b = map(int,input().split())
print(a*b)


#1008번 A/B
a, b = map(int,input().split())
print(a/b)

#10869번 사칙연산
a, b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b)) # 소수점 버리기 가능
print(a%b)

#10430번 나머지
A, B, C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


#2588번 곱셈
A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B[2])+A*int(B[1])*10+A*int(B[0])*100)