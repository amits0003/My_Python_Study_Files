# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

path = 'C:\\Users\\amit_pc\\Videos\\MAHABHARAT\\New folder\\'
dir_name = os.listdir(path)

print(dir_name)
# Function to rename multiple files
def main():
    for count, filename in enumerate(dir_name):
        print(filename)
        dst = "Mahabharat Episode  " + str( int(100+count) ) + ".mp4"
        src = path + filename
        dst = path + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
