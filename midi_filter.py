#from mido.midifies import MidiTrack
import mido

def main():
    """Simple filter to change message parameters (for debugging purposes)"""
    mid = mido.MidiFile('score5.mid')

    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for message in track:
            if not hasattr(message, 'velocity'):
                continue
            if message.velocity != 0:
                print "Changing velocity"
                message.velocity = 110
    mid.save('score5.mid')

if __name__ == "__main__":
    main()
