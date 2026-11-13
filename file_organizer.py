from pathlib import Path
import sys
import argparse

def put_in_dir(file:Path,new_dir_path:Path):
    i=1
    if (new_dir_path/file.name).exists()==True:
        k=new_dir_path/f'{file.stem}_1{file.suffix}'
        while(k.exists()):
            i+=1
            k=new_dir_path/f'{file.stem}_{i}{file.suffix}'
        print('The file:',file.name,'already existed so it has been renamed:',f'{file.stem}_{i}{file.suffix}')
        return file.rename(k)
    return file.rename(new_dir_path/file.name)

parser=argparse.ArgumentParser()
parser.add_argument('path',type=str,help='The path of the folder you want to organize')
parser.add_argument('--dry_run',help='Shows what changes would the porgram applies if it was ran',action='store_true')
args=parser.parse_args()
p=Path(args.path)
if not p.is_dir():
    print('Error, the path given is not a directory.')
    sys.exit(1)
    exit()
if args.dry_run:
    extension_set={file.suffix[1:].lower() if file.suffix != '' else 'Others'
                   for file in p.iterdir()}
    files_dict={ext: []for ext in extension_set}
    for file in list(p.iterdir()):
        if file.is_file():
            if file.name[0]=='.':
                continue
            elif file.suffix=='':
                files_dict['Others'].append(file.name)
            else:
                files_dict[file.suffix[1:].lower()].append(file.name)
    print('Only the files moved are showed,if the file is not showed below, it will not be organized')
    print(files_dict)
else:
    for file in list(p.iterdir()):
        if file.is_file():
            if file.name[0]=='.':
                continue
            elif file.suffix=='':
                (p/'Others').mkdir(exist_ok=True)
                new_dir_path=p/'Others'
                file= put_in_dir(file,new_dir_path)
            else:
                new_dir_path=p/file.suffix[1:].lower()
                new_dir_path.mkdir(exist_ok=True)
                file=put_in_dir(file,new_dir_path)

