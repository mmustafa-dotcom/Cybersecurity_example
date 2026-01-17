password=int(input("Enter Password:"))

for i in range(1000):
    print("Processing", i)

    if password==i:
        print("Password match", i)
        break

password1=int(input("Enter Password:"))
for a in range(100000):
    guess=str(a).zfill(4)
    print("Processing", guess)

    if password1==guess:
        print("Password match", guess)
        break
