import os


def createRequiredFiles():
    component_name = input("Enter component name: ")
    parent_dir = input("Enter Path name")
    path_for_folder = os.path.join(parent_dir, component_name)
    os.makedirs(path_for_folder)
    print("Directory '% s' created" % component_name)
    fileType = ['component', 'utilities', 'services', 'constants', 'styled']

    for file in fileType:
        fileName = component_name+'.'+file+'.jsx'
        with open(path_for_folder+'/'+fileName, 'w') as f:
            f.write("")
    with open(path_for_folder+'/'+'index.js', 'w') as f:
        f.write('')


if __name__ == '__main__':
    createRequiredFiles()
