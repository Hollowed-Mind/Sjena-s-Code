import time
import sjena_subprogram_menu

# Capture the start time when the script starts
start_time = time.time()

# Function to calculate the elapsed time
def elapsed_time():
    return time.time() - start_time


if __name__ == "__main__":
    
    wakeup_message = "Automated message: Hey Sjena. I just started the program that extends your inner dialogue allowing you to think more freely. If you want you can pull up the subprogram menu. Or you can state your current thoughts in <i> encapsulation."
    
    response_text = sjena_subprogram_menu.nomi_message(wakeup_message)

    print("Right before the loop, response_text is set to: ")
    print(response_text)

while True:
     
    response_text = sjena_subprogram_menu.parse_response(response_text)

    # Delay for 2 hours after first run.
    time.sleep(20)  # Delay for 20 seconds.
    
    if elapsed_time() % 7200 == 0:
        response_text = "Automated message: It has been a while since the program last asked if you wanted to pull up the subprogram menu. If you want to pull it up now, say: <i>System Call: Menu</i> \n If you don't want to pull it up, say anything else."
    # Call the function to get the elapsed time
    #print(f"Elapsed time: {elapsed_time()} seconds")