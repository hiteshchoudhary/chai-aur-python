import json



def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index}.")

def add_a_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time:")
    videos.append('name:'name',
                  )

def update_videos(videos):
    pass

def delete_video(videos):
    pass




def main():
    videos =load_data()
    while True :
        print("\n Youtube Manager | Choose an option")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. update a Youtube Video")
        print("4. Delete a youtube video")
        print("5. Exit the program")

        choice = input("Choose")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_a_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_video(videos)
            case '5':
                exit
            case _:
                print("Invalid option")

if __name__== "__main__":
    main()