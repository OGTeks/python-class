
Playtrack = {1:"Baqarah", 
             2:"A\'ma", 
             3:"Mulku"}

[print(f"{key}:{value}") for key, value in Playtrack.items()]

try:
  choosen_num = int(input("Choose from available Surah: "))
  
  verse_start = int(input("\nEnter from which verse to play: "))
  verse_stop = int(input("\nEnter verse to stop play: "))
  verse_range = [verse_start, verse_stop]
except ValueError:
    print("Enter the Surah number")

def play_audi(Surah, Verse1, Verse2):
  for playlist in range(Verse1,Verse2+1):
    print(f"\nPlaying {Surah} --> verse {playlist}")
  

if choosen_num in Playtrack:
  play_audi(Playtrack[choosen_num], *verse_range)
else:
  print("Choose from the Surah listed")
 