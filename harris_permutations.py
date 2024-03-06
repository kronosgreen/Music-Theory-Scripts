import argparse
import musicpy as music
import itertools


parser = argparse.ArgumentParser(description='Harris Permutations')

parser.add_argument('chord_1', type=str, help='First chord')
parser.add_argument('chord_2', type=str, help='Second chord')

args = parser.parse_args()

chord_1 = music.C(args.chord_1)
chord_2 = music.C(args.chord_2)

notes_1 = chord_1.notes
notes_2 = chord_2.notes

print(type(notes_1[0]).note)

print(f"First Chord: {args.chord_1}: {notes_1}")
print(f"First Chord: {args.chord_2}: {notes_2}")

print(f"Permutations:")
for first_chord in itertools.combinations(notes_1 + notes_2, r=4):
    second_chord = [x for x in notes_1 + notes_2 if x not in first_chord]
    print(f"{list(first_chord)}, {second_chord}")
