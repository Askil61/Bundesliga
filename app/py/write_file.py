from glob import glob
def write_xml_file(filename: str, ext: str, path: str, data: str) -> None:
    with open(f"{path}bundesliga_{filename}.{ext}", "w") as file:
        file.write(data)
        file_path = str(*glob(f"out/*{filename}*.xml"))
        print(f'created file -> {file_path}')

if __name__ == '__main__':
    pass
