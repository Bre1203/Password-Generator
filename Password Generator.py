import random

password_list={
"Passwords":("1Ki77y", ".Susan53", "jelly22fi$h", "$m3llycat", "a11Black$", "!ush3r", "&ebay.44", "d3ltagamm@", "!Lov3MyPiano", "SterlingGmail20.15", "BankLogin!3")}


category = random.choice(list(password_list.keys()))
word = (random.choice(password_list[category]))

print("Welcome! I will pick a new password for you.")
print(word+ " is your new password!")
