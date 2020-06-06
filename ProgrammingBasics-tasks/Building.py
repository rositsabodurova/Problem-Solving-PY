floor_count = int(input())
room_count = int(input())

if room_count == 1:
    for i in range(0, room_count):
        print(f"L{floor_count}{i}", end=" ")
    print()
else:
    for i in range(floor_count, 0, -1):
        for j in range(0, room_count):
            if i == floor_count:
                print(f"L{floor_count}{j}", end=" ")
            else:
                if i % 2 == 0:
                    print(f"O{i}{j}", end=" ")
                else:
                    print(f"A{i}{j}", end=" ")
        print()