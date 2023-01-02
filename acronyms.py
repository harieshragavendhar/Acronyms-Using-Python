A = input()
b = input()
phrase = (A.replace('of', '')).split()
acronym = ""
for word in phrase:
  acronym=acronym + word[0].upper()
  print(acronym,end="")