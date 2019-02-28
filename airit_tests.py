"""
Tate Dyer
Lab 9
"""
from airit_simulation import *

def test_read_passenger():
    with open("passengers_very_small.txt") as f:
        for line in f:
            passenger=read_passenger(line)
            print(passenger)

def test_line_up():
    gate=Gate(mkEmptyQueue(), mkEmptyQueue(), mkEmptyQueue(), mkEmptyQueue(), 0, 8)
    file=open("passengers_very_small.txt")
    line_up(gate, file, 5)
    print("Simulation complete; all passengers are at their destinations!")
    file.close()
    print(gate.people==gate.max)


def main():
    test_read_passenger()
    test_line_up()

if __name__ == '__main__':
    main()

