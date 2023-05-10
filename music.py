from music21 import *

#create a score for the music to be written in
score = stream.Score()

#create a time signature to show how many beats will be in a measure
score.append(meter.TimeSignature('4/4'))

#create a series of notes that will be in our score
score.append(note.Note('C4'))
score.append(note.Note('D4'))
score.append(note.Note('E4'))
score.append(note.Note('F4'))
score.append(note.Note('G4'))
score.append(note.Note('A4'))
score.append(note.Note('B4'))
score.append(note.Note('C5'))

#show the results in a written form of the score
score.show()

# show the results in audio form
#score.show('midi')

# #_______________________________________________________________________________________________#

# #create a new score to stream
# s = stream.Stream()

# #create a time signature to show how many beats will be in a measure
# s.insert(meter.TimeSignature('6/8'))

# # #set the key signature of the song
# A = key.KeySignature(3)
# s.append(A)

# #set the tempo for the song
# t = tempo.MetronomeMark('slow', 60, note.Note(type='quarter'))
# s.append(t)

# #create the different parts to add to the stream
# part1 = stream.Part()
# part2 = stream.Part()
# part3 = stream.Part()
# part4 = stream.Part()

# #create the notes for the first part
# notes1 = [note.Note("A5"), note.Note("G#5"), note.Note("E5"), note.Note("C#5"), note.Note("E5"), note.Note("F#5")]

# #setting length for the notes
# for n in notes1:
#     n.duration.type = "whole"

# #appending the notes to the first part
# for n in notes1:
#     part1.append(n)

# #creating the notes for the second part
# notes2 = [note.Note("C#4"), note.Note("B3"), note.Note("C#4"), note.Note("C#4"), note.Note("C#4"), note.Note("A3")]

# #setting length for the notes
# for n in notes2:
#     n.duration.type = "whole"
  
# #appending the notes to the second part
# for n in notes2:
#     part2.append(n)

# #creating the notes for the third part
# notes3 = [note.Note("A3"), note.Note("G#3"), note.Note("A3"), note.Note("A3"), note.Note("A3"), note.Note("F#3")]

# #setting length for the notes
# for n in notes3:
#     n.duration.type = "whole"
  
# #appending the notes to the second part
# for n in notes3:
#     part3.append(n)

# #creating the notes for the fourth part
# notes4 = [note.Note("F#3"), note.Note("E3"), note.Note("E3"), note.Note("F#3"), note.Note("E3"), note.Note("D3")]

# #setting length for the notes
# for n in notes4:
#     n.duration.type = "whole"
  
# #appending the notes to the second part
# for n in notes4:
#     part4.append(n)

# #inserting all the parts into the score at the 0th measure (beginning)
# s.insert(0, part1)
# s.insert(0, part2)
# s.insert(0, part3)
# s.insert(0, part4)

# #showing the score in the MuseScore Software
# s.show()

