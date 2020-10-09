print('conversor de temperaturas')
i=0
i= float(input('1- C°    2- F°'))
if i== 1 :
  f1 = float(input('DIGITE O VALOR QUE QUER CONVERTER DE F° PARA C°'))
  c1= (f1-32)/1.8
  print('O valor em c° é:',c1)
elif i==2:
  c2 = float(input('DIGITE O VALOR QUE QUER CONVERTER DE F° PARA C°'))
  f2=(1.8*c2)+32
  print('O valor em F° é:',f2)

  