import json
import os
import uuid
import time

def gen_uuid(name_string):
    seed = f"{name_string}{int(time.time() * 1000)}"
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, seed))

def main():
    notifications_file_path = os.path.abspath('notifications.json')

    os.system('cls' if os.name == 'nt' else 'clear')

    print("--- New Notification ---")
    title = input("Notification title: ")
    body_input = input("Notification body: ")

    body = body_input.replace('\\n', '\n')

    new_notification = {
        "title": title,
        "body": body,
        "uuid": gen_uuid(title)
    }

    try:
        if os.path.exists(notifications_file_path):
            with open(notifications_file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                notifications = json.loads(data) if data.strip() else []
            
            notifications.append(new_notification)
            
            with open(notifications_file_path, 'w', encoding='utf-8') as f:
                json.dump(notifications, f, indent=4)
            print('Notification added successfully!')
        else:
            # Equivalent to ENOENT block
            initial_data = [new_notification]
            with open(notifications_file_path, 'w', encoding='utf-8') as f:
                json.dump(initial_data, f, indent=4)
            print('Notification added successfully! (New file created)')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
