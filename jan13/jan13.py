num = []
while True:
  print('''
            Enter a value either float or integer that you wish
            to add. Input "q" when you are done inputting
             all the numbers.
        ''')
        
      

  user_input = input("Enter one value: ")

  if user_input.isdigit():
      num.append(int(user_input))
  else:
      try:
        int_value = int(user_input)
        num.append(int(user_input))
      except ValueError:
        if user_input.lower().strip() == 'q':
          print(sum(num))
          break





   