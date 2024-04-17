import time


class Sender:
    def __init__(self):
        self.window_size = 0
        self.timeout = 10
        self.window_start = 0
        self.window_end = 0
        self.packets = []
        self.acknowledges = []



def initialize_sender():
    nr_of_packets = int(input("Enter the number of packets: "))
    sender.window_size = int(input("Enter the window size: "))
    
    for i in range(nr_of_packets):
        sender.packets.append(i+1)
    
    sender.window_end = sender.window_size - 1
    
def timer(seconds):
    print("Timer started for", seconds, "seconds.")
    time.sleep(seconds)
    print("Timer completed.")
    
def resend_packet():
    global lost_packet
    for i in range(sender.window_start, sender.window_end + 1):
            if sender.packets[i] not in Reciever:
                print("Packet", sender.packets[i], "is sent.")
                if(sender.packets[i] == 3 and lost_packet == False):
                    lost_packet = True
                    print("Packet 3 is lost.")
                else:
                    Reciever.append(sender.packets[i])
    
def sliding_window():
    beginning = sender.window_start
    global lost_packet
    global lost_ack
    
    while sender.window_end < len(sender.packets):
        print("Window start:", sender.window_start)
        print("Window end:", sender.window_end)
        print("Packets in window:", sender.packets[sender.window_start:sender.window_end + 1])
        print("Reciever:", Reciever)
        print("Acknowledges:", sender.acknowledges)
        for i in range(sender.window_start, sender.window_end + 1):
            if sender.packets[i] not in sender.acknowledges and sender.packets[i] > beginning:
                print("Packet", sender.packets[i], "is sent.")
                if(sender.packets[i] == 3 and lost_packet == False):
                    lost_packet = True
                    print("Packet 3 is lost.")
                    
                else:
                    Reciever.append(sender.packets[i])
                    print("Packet", sender.packets[i], "is received.")
                beginning += 1
                
        if sender.packets[sender.window_start] in Reciever:
            ack_to_send = sender.packets[sender.window_start]
            print("Acknowledgement for packet", ack_to_send, "is sent.")
            if(ack_to_send == 5 and lost_ack == False):
                lost_ack = True
                print("Acknowledgement for packet 5 is lost.")
            else:
                sender.acknowledges.append(ack_to_send)
            
        if sender.packets[sender.window_start] in sender.acknowledges:
            sender.window_start += 1
            sender.window_end += 1
            if sender.window_end >= len(sender.packets):
                sender.window_end = len(sender.packets) - 1
            if sender.window_start >= len(sender.packets):
                break
        else:
            print("Waiting for acknowledgement for packet", sender.packets[sender.window_start])
            timer(sender.timeout)
            print("Timeout for packet", sender.packets[sender.window_start], "occured.")
            resend_packet()
            
  
def main():
    global sender
    global lost_packet 
    global lost_ack
    global Reciever
    Reciever = []
    lost_packet = False
    lost_ack = False
    sender = Sender()
    initialize_sender()
    print(sender.packets)
    print(sender.window_start)
    print(sender.window_end)
    print(sender.timeout)
    print(sender.acknowledges)
    print(sender.window_size)
    print()
    sliding_window()
    print()
    print("Reciever: ",Reciever)
    print()
    print()
    Reciever.sort()
    print("Reciever: ",Reciever)
    
if __name__ == "__main__":
    main()