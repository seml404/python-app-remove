import os



ts_folder = "/Code/type-script-course/src"
ts_content = os.scandir(ts_folder)


def check_and_delete(file, target_folder):
    if os.path.isfile(file) and (str(file).find('.js')>0 or str(file).find('.js.map')>0 or str(file).find('.d.ts')>0 ):
        print('file', file, os.path.join( target_folder, file))
        os.remove(os.path.join(target_folder, file))

def remove_js(folder_name):
    subfolders = []
    for item in folder_name:
        if os.path.isdir(item):
            subfolders.append(item);
            print(subfolders)

    for subfolder in subfolders:
        files = os.scandir(subfolder)
        for file in files:
            check_and_delete(file, subfolder);





remove_js(ts_content);
