from pathlib import Path
import sys
import argparse

def put_in_dir(file:Path,new_dir_path:Path,dry_run:bool):
    i=1
    if (new_dir_path/file.name).exists()==True:
        k=new_dir_path/f'{file.stem}_1{file.suffix}'
        while(k.exists()):
            i+=1
            k=new_dir_path/f'{file.stem}_{i}{file.suffix}'
        if dry_run:
            print(f'{file.name} --> {new_dir_path.name}/{file.stem}_{i}{file.suffix}')
        else:
            print(f'The file: {file.name} already existed so it has been renamed: {file.stem}_{i}{file.suffix}')
            return file.rename(k)
    else:
        if dry_run:
            print(f'{file.name} --> {new_dir_path.name}/{file.name}') 
        else:
            return file.rename(new_dir_path/file.name)

parser=argparse.ArgumentParser()
parser.add_argument('path',help='The path of the folder you want to organize')
parser.add_argument('--dry-run',help='Show what would be moved without moving anything',action='store_true')
args=parser.parse_args()
p=Path(args.path)
if not p.is_dir():
    print('Error, the path given is not a directory.')
    sys.exit(1)
if args.dry_run:
    dry_run=True
    for file in list(p.iterdir()):
        if file.is_file():
            if file.name[0]=='.':
                continue
            elif file.suffix=='':
                new_dir_path=p/'Others'
                put_in_dir(file,new_dir_path,dry_run)
            else:
                new_dir_path=p/file.suffix[1:].lower()
                put_in_dir(file,new_dir_path,dry_run)
else:
    dry_run=False
    for file in list(p.iterdir()):
        if file.is_file():
            if file.name[0]=='.':
                continue
            elif file.suffix=='':
                (p/'Others').mkdir(exist_ok=True)
                new_dir_path=p/'Others'
                file= put_in_dir(file,new_dir_path,dry_run)
            else:
                new_dir_path=p/file.suffix[1:].lower()
                new_dir_path.mkdir(exist_ok=True)
                file=put_in_dir(file,new_dir_path,dry_run)

