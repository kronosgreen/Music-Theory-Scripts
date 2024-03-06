import argparse
import musicpy as music
import itertools


parser = argparse.ArgumentParser(description="Following Barry Harris's teachings, takes two four note chords " + \
                                 "and finds all possible 4 note chord combinations of the combined notes.")

parser.add_argument('chord_1', type=str, help='First chord e.g. Cmaj7, Dm7, etc.')
parser.add_argument('chord_2', type=str, help='Second chord')

args = parser.parse_args()

chord_1 = music.C(args.chord_1)
chord_2 = music.C(args.chord_2)

notes_1 = chord_1.notes
notes_2 = chord_2.notes

print(f"First Chord: {args.chord_1}: {notes_1}")
print(f"Second Chord: {args.chord_2}: {notes_2}")

print("\nPermutations:")
for first_chord in itertools.combinations(notes_1 + notes_2, r=4):
    second_chord = [x for x in notes_1 + notes_2 if x not in first_chord]
    print(f"{list(first_chord)}, {second_chord}")
