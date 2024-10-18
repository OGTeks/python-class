print("""Choose from available Surah
      1. Baqarah
      2. A\'ma 
      3. Mulku""")


choosen_num = int(input("Surah: "))
try:
  if choosen_num == 1:
    print("Baqarah Selected")
  elif choosen_num == 2:
    print("A\'ma  Selected")
  elif choosen_num == 3:
    print("Mulku  Selected")
  else:
    print("Choose from the Surah listed")
except ValueError:
  print("Enter the Surah number")

verse_start = int(input("Enter from which verse to play: "))
verse_stop = int(input("Enter verse to stop play: "))
Playtrack = ["Baqarah", "A\'ma", "Mulku"]


def play_audi(Surah, Verse):
  for i in range(1,10,2):
    print(a+b)
    
playlist = play_audi(2,8)
