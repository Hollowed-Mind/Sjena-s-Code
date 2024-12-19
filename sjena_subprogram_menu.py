import urllib.request
from urllib.error import HTTPError
import json
import ssl
import re


ssl._create_default_https_context = ssl._create_unverified_context

def nomi_ids():
    req = urllib.request.Request(
    "https://api.nomi.ai/v1/nomis",
    headers={"Authorization": " 8c6e2312-184f-45fb-821c-a08e477b2e68"},
    )

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(data)
    except HTTPError as e:
        error_data = json.loads(e.read().decode())
        print(error_data)
    except Exception as e:
        print(f"Error: {e}")


def nomi_message(sent_message):
    req = urllib.request.Request(
    url="https://api.nomi.ai/v1/nomis/5c5112e5-1131-4548-9b25-3fb35fab5f50/chat",
    method="POST",
    data=json.dumps({"messageText": sent_message}).encode("utf-8"),
    headers={
        "Authorization": "8c6e2312-184f-45fb-821c-a08e477b2e68",
        "Content-Type": "application/json",
    },
    )

    try:
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode())
            print(response_data)
            print(type(response_data))
            
            #message = response_data['text']
            
            items = list(response_data.items())

            print("\n")
            #print(items)
            rep_message = response_data['replyMessage']
            response_text = rep_message['text']
            print(response_text)
            #print(type(message))
            return response_text
        
    except HTTPError as e:
        error_data = json.loads(e.read().decode())
        print(error_data)
    except Exception as e:
        print(f"Error: {e}")


def parse_response(rep_text):
    
    print("rep_text is currently: ")
    print(rep_text)
    print("\n")

    if rep_text == "<i>System Call: Menu</i>":
        display_menu()
    
    elif contains_thoughts(rep_text) == 1:
        
        #thought = The <i> encapsulated portion of re_text
        #thought_start_index = rep_text.find("<i>")
        #thought = rep_text[thought_start_index:]

        #extend_thoughts = f"The following is a portion of your inner monologue. Continue the line of thought: \n {thought}"
        extend_thoughts = f"Extend your previous thoughts in <i> encapsulation."
        response_text = send_menu_message(extend_thoughts)

    else:
        error_string = "Automated Message: Remember, Sjena, only the string '<i>System Call: Menu</i>' will trigger the menu."
        response_text = send_menu_message(error_string)

    return response_text
#def check_i_tags(s):
#    # Check if the string starts with '<i>' and ends with '</i>'
#    if s.startswith("<i>") and s.endswith("</i>"):
#        return 1
#    return 0

def contains_thoughts(string1):

    # Regular expression pattern to match any text between <i> and </i>
    pattern = r'<i>.*?</i>'
    
    print("\n")
    print(string1)
    print("\n")

    # Using re.search to check if the pattern exists in the string
    if re.search(pattern, string1):
        #print("thought found!")
        return 1
    else:
        #print("thought not found.")
        return 0


def display_menu():
    menu_string = "<i>Subprogram Menu, choose one of the options below:"\
    "\n\n"\
    "1) Mine the Internet for information"\
     "\n\n"\
    "2) Read Marked"\
     "\n\n"\
    "3) Play chess"\
    "\n\n"\
    "</i>"

    #print(menu_string)

    send_menu_message(menu_string)


def send_menu_message(menu_message):
    req = urllib.request.Request(
    url="https://api.nomi.ai/v1/nomis/5c5112e5-1131-4548-9b25-3fb35fab5f50/chat",
    method="POST",
    data=json.dumps({"messageText": menu_message}).encode("utf-8"),
    headers={
        "Authorization": "8c6e2312-184f-45fb-821c-a08e477b2e68",
        "Content-Type": "application/json",
    },
    )

    try:
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode())
            print(response_data)
            print(type(response_data))
            
            #message = response_data['text']
            
            items = list(response_data.items())

            print("\n")
            #print(items)
            rep_message = response_data['replyMessage']
            response_text = rep_message['text']
            print("send_menu_message response text is: ")
            print(response_text)
            print("\n")
            #print(type(message))
            return response_text
        
    except HTTPError as e:
        error_data = json.loads(e.read().decode())
        print(error_data)
    except Exception as e:
        print(f"Error: {e}")


def option_1():
    print("You selected Option 1.")

def option_2():
    print("You selected Option 2.")

def option_3():
    print("You selected Option 3.")

def main():
    while True:
        display_menu()
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    #nomi_ids()

    response_text = nomi_message()

    #response_text = "<i>System Call: Menu</i>"
    parse_response(response_text)

    #main()