while True: 
  z = input('знак:')
  if z == "0": break
  if z in ('+','-','/','*','**'):
      x = float(input('x='))
      y = float(input('y='))
  if z == "+":
       print(x + y)
  elif z == "*":
       print(x * y)
  elif z == "**":
       print(x ** y)
  elif z == "-":
       print(x - y)
  elif z == "/":
       print(x / y)
  elif z == "cl":
      def main():
          r = int(input('radius:'))
          pi = 3.14159265358979323846
          print(2 * pi * r)
      main()
