import sys

def GT(x):
  if 'liala' in x or 'etra' in x or 'inites' in x:
    return 1
  if 'lios' in x or 'etr' in x or 'initis' in x:
    return 2
  else:
    return 0
def VT(y):
  x=0
  c=0
  flag=0
  for i in y:
    if 'etra' in i or 'etr' in i:
      x=c
      flag+=1
    c+=1
  if flag >1: return False
  if 'initis' in y[x-1] or 'inites' in y[x-1]: return False
  if 'lios' in y[x+1] or 'liala' in y[x+1]: return False
  return True

s= 'nataliala kataliala vetra feinites'
a=s.split()
if len(a)<2:
if 'lios' in s or 'etr' in s or 'initis' in s or 'liala' in s or 'etra' in s or 'inites' in s:
    print('YES')
   else:
   	print('NO') 
	sys.exit()
#kiem tra gioi tinh
for i in range(1,len(a)):
  if GT(a[i])!=GT(a[i-1]) or GT(a[i])==0:
    print('NO')
    sys.exit()
#kiem tra vi tri danh tu
if VT(a) == False:
  print('NO')
else:
  print('YES')
