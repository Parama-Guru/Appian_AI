import os 



def delete_previous_file(save_dir):
    for file_name in os.listdir(save_dir):
        if file_name.endswith('.pdf'):
            os.remove(os.path.join(save_dir, file_name))