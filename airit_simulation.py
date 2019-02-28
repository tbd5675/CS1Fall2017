"""
Tate Dyer
Lab 9
"""
from myQueue import *
from myStack import *
from rit_lib import *

Passenger=struct_type("Passenger", (str, "name"), (str, "ticket"), (bool, "bag"))
def make_passenger(name,ticket,bag):
    return Passenger(name,ticket,bag)
Gate= struct_type("Gate", (Queue,"zone1"), (Queue,"zone2"), (Queue,"zone3"), (Queue,"zone4"), (int, "people"), (int,"max"))
AirIT=struct_type("AirIT", (Stack, "has_bag"), (Stack, "no_bag"), (int, "passengers"), (int, "max"))

def read_passenger(file):
    """
    given file creates a passenger by splitting the line up
    :param file: input file
    :return:
    """
    if file=="":
        return None
    else:
        line=file.strip()
        line=line.split(",")
        return make_passenger(line[0],line[1], line[2]=="True")

def line_up(gate,file, max_plane):
    """
    calls read passenger to create them one at a time as they are put into a zone at the gate according to their ticket number
    :param gate: structure that contains the zones  as a queues
    :param file: input file
    :param max_plane: input max of plane
    :return:
    """
    print("Passengers are lining up at the gate...")
    for line in file:
        if gate.people==gate.max:
            print("The gate is full; remaining passengers must wait.")
            if emptyQueue(gate.zone4) is True and emptyQueue(gate.zone3) is True and emptyQueue(
                    gate.zone2) is True and emptyQueue(gate.zone1) is True:
                print("The last passenger is in line!")
            load_plane(gate, gate.people, max_plane)
        else:
            passenger = read_passenger(line)
            gate_num = passenger.ticket[0]
            if gate_num=='1':
                enqueue(gate.zone1, passenger)
                gate.people+=1
            elif gate_num=='2':
                enqueue(gate.zone2, passenger)
                gate.people += 1
            elif gate_num=='3':
                enqueue(gate.zone3, passenger)
                gate.people += 1
            else:
                enqueue(gate.zone4, passenger)
                gate.people += 1
            print(passenger)

def load_plane(gate, people, max_plane):
    """
    loads the plane with passengers starting with zone 4 and descending and when full takes off and comes back for others later
    :param gate: contains the zones containing people
    :param people: number of people in all the gates
    :param max_plane: max num of people allowed on plane at a time
    :return:
    """
    print("Passengers are boarding the aircraft...")
    plane=AirIT(mkEmptyStack(), mkEmptyStack(), people, max_plane)
    while emptyQueue(gate.zone4)==False or plane.passengers==plane.max:
        passenger=front(gate.zone4)
        if passenger.bag is False:
            push(plane.no_bag, passenger)
            plane.passengers+=1
        else:
            push(plane.has_bag, passenger)
            plane.passengers += 1
        print(passenger)
        dequeue(gate.zone4)
    while emptyQueue(gate.zone3)==False or plane.passengers==plane.max:
        passenger=front(gate.zone3)
        if passenger.bag is False:
            push(plane.no_bag, passenger)
            plane.passengers+=1
        else:
            push(plane.has_bag, passenger)
            plane.passengers += 1
        print(passenger)
        dequeue(gate.zone3)
    while emptyQueue(gate.zone2)==False or plane.passengers==plane.max:
        passenger=front(gate.zone2)
        if passenger.bag is False:
            push(plane.no_bag, passenger)
            plane.passengers+=1
        else:
            push(plane.has_bag, passenger)
            plane.passengers += 1
        print(passenger)
        dequeue(gate.zone2)
    while emptyQueue(gate.zone1)==False or plane.passengers==plane.max:
        passenger=front(gate.zone1)
        if passenger.bag is False:
            push(plane.no_bag, passenger)
            plane.passengers+=1
        else:
            push(plane.has_bag, passenger)
            plane.passengers += 1
        print(passenger)
        dequeue(gate.zone1)
    print("Passengers are disembarking...")
    unload_plane(plane)

def unload_plane(plane):
    """
    once plane arrives drops off everyone so it can go back for another load
    :param plane: structure that contains stacks of people
    :return:
    """
    while emptyStack(plane.no_bag) is False:
        print(top(plane.no_bag))
        pop(plane.no_bag)
    while emptyStack(plane.has_bag) is False:
        print(top(plane.has_bag))
        pop(plane.has_bag)


def main():
    file=input("Passenger data file: ")
    max_gate=int(input("Gate capacity: "))
    max_plane=int(input("Aircraft capacity: "))
    gate=Gate(mkEmptyQueue(), mkEmptyQueue(), mkEmptyQueue(), mkEmptyQueue(), 0, max_gate)
    with open(file) as f:
        line_up(gate, file, max_plane)
    print("Simulation complete; all passengeres are at their destinations!")

if __name__ == '__main__':
    main()