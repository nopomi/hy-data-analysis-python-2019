#!/usr/bin/env python3
import re

def file_extensions(filename):

    with open(filename) as f:
        ext = {}
        non_ext = []
        for name in f:
            match = re.match(r'(.+)\.(.+)\n',name)
            if match:
                if match.group(2) in ext:
                    ext[match.group(2)].append(match.group(0)[:-1])
                else:
                    ext[match.group(2)] = [match.group(0)[:-1]]
            else:
                non_ext.append(name[:-1])
    return (non_ext, ext)

def main():
    non_ext, ext = file_extensions("src/filenames.txt")
    print(f"{len(non_ext)} files with no extension")
    for key in ext:
        print(f"{key} {len(ext[key])}")

if __name__ == "__main__":
    main()
