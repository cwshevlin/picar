import picar_4wd as fc
import random
import time

speed = 10

def random_choice():
    return random.choice([True, False])

def random_int(max):
    return random.randint(1, max)

def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print("SCAN LIST TMP")
        print(tmp)
        if tmp != [2,2,2,2]:
            fc.stop()
            time.sleep(.1)
            fc.backward(speed * 2)
            time.sleep(.5)
            fc.stop()
            time.sleep(.1)
            if random_choice():
                fc.forward(speed)
                fc.turn_right(speed)
            else:
                fc.forward(speed)
                fc.turn_left(speed)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
