# -*- coding: utf-8 -*-
average_sales = list(map(float,input().split()))
n = int(input())
v = float(input())
c = int(input())
def prediction(a):
  for i in a:
    if len(a) == n:
      x = sum(a)/n
      return x
    if len(a) != n:
      z = a[-n:]
      x = sum(z)/n
      return x
d = prediction(a=average_sales)
u = sum(average_sales)/len(average_sales)
s = []
s.append(u)
for j in range(len(average_sales)):
  q = 0
  q + 1
  g = v*int(average_sales[q]) +(1-v)*int(s[q])
  s.append(g)
l = (c-int(d))
p = int(s[-1])
e1 = float((abs(l)/c)*100)
k = (c-p)
e2 = float((abs(k)/c)*100)
print(round(d))
print(round(s[-1]))
if e1<e2:
  h = "%.3f" % e1
  print(f'Forecasting method1 is more optimized with {h} error percentage')
else:
  o = "%.3f" % e2
  print(f'Forecasting method2 is more optimized with {o} error percentage')
if e1 == e2 :
  print(f'Either meth0d is viable with {o} error percentage')