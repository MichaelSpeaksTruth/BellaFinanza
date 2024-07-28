import os

# Specify the path for the new folder
new_folder_path = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server\noname"

# Create the folder
os.mkdir(new_folder_path)


def new_folder(new_folder_name):
    new_folder_path = r"D:\Delvitide Industries Private Limited\Rt-Ant Development House\Bella Finanza\Server"+"\\"+new_folder_name
    os.mkdir(new_folder_path)