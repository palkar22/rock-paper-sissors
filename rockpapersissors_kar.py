import random
L1=["rock","paper","scissor"]
PC_input=random.choice(L1)

n=int(input("""0 for rock
1 for paper
2 for scissor
"""))

user_input=L1[n]
print("pc choice:",PC_input)
print("your choice:",user_input)
if user_input=='rock' and PC_input=='paper':
  print("PC wins")
elif user_input=="rock" and PC_input=='scissor':
  print("user wins")
elif user_input=="paper" and PC_input=='scissor':
  print("PC wins")
elif user_input=="paper" and PC_input=='rock':
  print("user wins")
elif user_input=="scissor" and PC_input=='rock':
  print("PC wins")
elif user_input=="scissor" and PC_input=='paper':
  print("user wins")
else:
  print("draw")