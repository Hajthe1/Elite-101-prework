def chatbot():
  print("welcome to elite 101 chatbot")
  name = input("what is your name? ")
  while True:
    try:
      age = int(input("Welcome " + name + " , how old are you? "))
      if age > 1:
        break
      else:
        print("please be realistic")
    except ValueError:
      print("please be realistic")
  print("It must be nice being", age)
  while True:
    print("1. Option 1")  
    print("2. Option 2")  
    print("3. Exit")
    choice = int(input("How may I help you today?"))
    if choice == 1 or choice == 2:
      print("I dont have anything yet")
      break
    elif choice == 3:
      print("Have a good day, and I hope I was helpful.")
      break
    else:
      print("Invalid choice")
chatbot()