from pathlib import Path
def put_in_dir(file:Path,new_dir_path:Path):
    i=1
    if (new_dir_path/file.name).exists()==True:
        k=new_dir_path/f'{file.stem}_1{file.suffix}'
        while(k.exists()):
            i+=1
            k=new_dir_path/f'{file.stem}_{i}{file.suffix}'
        print('Il file:',file.name,'esisteva gia dentro la cartella, quindi e stato rinomianto e chiamato:',f'{file.stem}_{i}{file.suffix}')
        return file.rename(k)
    return file.rename(new_dir_path/file.name)
try:
    p=Path(input('Inserisci il path della cartella di cui vuoi ordinare i files:'))
    for file in list(p.iterdir()):
        if file.is_file():
            if file.name[0]=='.':
                continue
            elif file.suffix=='':
                (p/'Altro').mkdir(exist_ok=True)
                new_dir_path=p/'Altro'
                file= put_in_dir(file,new_dir_path)
            else:
                new_dir_path=p/file.suffix[1:].lower()
                new_dir_path.mkdir(exist_ok=True)
                file=put_in_dir(file,new_dir_path)
except FileNotFoundError:
    print('Il Path fornito non esiste, riprovare.')
