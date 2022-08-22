st = input("enter something")
s1 = st.lower()
s2 = reversed(s1)
if list(s1) == list(s2):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
exit()