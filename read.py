def main():
     f= open("read_file.txt","r+")
     if f.mode == "r":
         contents = f.read()
         print(contents)
if __name__== "__main__":
  main()

