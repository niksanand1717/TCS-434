lst = list(map(str, input("Enter contents of list: ").lower().split()))
print("Contents of list in  lowercase :", lst)
print("Result after removing duplicate elemrnts:", list(set(lst)))