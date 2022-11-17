path_with_extension = input().split("\\")

filename, extension = path_with_extension[-1].split(".")

print(f"File name: {filename}\n"
      f"File extension: {extension}")