def activity_function():
  print("Please enter an activity")
  print("1. Watch Movie")
  print("2. Play")
  print("3. Other (Please tell me what to do...)")
  activity = str(input())
  if activity == "1":
    print("Watching a movie sounds like fun.")
  elif activity == "2":
    print("I have lots of toys to play with.")
  else:
    print("I am not sure if I will like it but I will give it a try.")
activity_function()
