file = open("hello.txt", "a")
texts=[f"line{char+1}\n"for char in range(10)]

print(file.writelines(texts))


file.close()
      