import queue

queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request {request_id}"
    queue.put(request)
    print(f"✅ Generated and added: {request}")
    
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"🔧 Processing: {request}")
    else:
        print("⚠️ Queue is empty. Nothing to process.")
    
def main():
    while True:
        action = input("\nChoose action: [1] Generate [2] Process [3] Exit: ")

        if action == "1":
            generate_request()
        elif action == "2":
            process_request()
        elif action == "3":
            print("Exiting program.")
            break
        else:
            print("❓ Unknown action. Please choose 1, 2, or 3.")
            
if __name__ == "__main__":
    main()