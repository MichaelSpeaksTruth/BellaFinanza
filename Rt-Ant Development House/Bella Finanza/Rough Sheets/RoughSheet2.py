import time
import sys
print("")print("")
def animate_processing():
    dots = ['.   ', '..  ', '... ', '....', '.....','......','.......','........']
    for i in range(4):  # Loop through the animation frames
        sys.stdout.write('\rProcessing' + dots[i % len(dots)])
        sys.stdout.flush()
        time.sleep(0.5)  # Pause for half a second

print("Welcome to Money Equilibrium")
time.sleep(2)  # Pause for 2 seconds to display the welcome message
animate_processing()