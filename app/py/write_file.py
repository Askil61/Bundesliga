
def write_xml_file(filename: str, ext: str, path: str, data: str) -> None:
    with open(f"{path+filename}.{ext}", "w") as file:
        file.write(data)
        print(f"file {path+filename}.{ext} created")

if __name__ == '__main__':
    pass
