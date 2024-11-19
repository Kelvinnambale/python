f_source = open("source.png" "rb")
f_dest = open("dest.png" "wb")

char_count = 0

for line in f_source:
    char_count += len(line)
    f_dest.write(line)
print(char_count, "characters copied successful")

f_source.close()
f_dest.close()