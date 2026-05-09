from pathlib import Path

path = Path.home() / "hello.txt"
path.touch()


file = path.open(mode= "r", encoding= "utf-8") #encoding and reading mode
file.close() #close once done

file_path = path
file = open(file_path, mode="r", encoding="utf-8")
file.close() #close once done

with path.open(mode= "r", encoding= "utf-8") as file:
    for line in file.readlines():
        print(line, end="")
        #text = file.read()

file.close() #close once done


with path.open(mode= "w", encoding= "utf-8") as file:
    file.write("Hi there!")
file.close() #close once done


with path.open(mode= "a", encoding= "utf-8") as file:
    file.write("\nHello")
file.close() #close once done




with path.open(mode= "r", encoding= "utf-8") as file:
    text = file.read()
    print(text)
path.unlink()