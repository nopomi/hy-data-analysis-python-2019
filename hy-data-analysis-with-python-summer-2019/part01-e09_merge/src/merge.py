#!/usr/bin/env python3

def merge(L1, L2):
    merged_list = []
    list1 = L1.copy()
    list2 = L2.copy()
    for i in range(len(list1) + len(list2)):
        if len(list1) > 0 and len(list2) > 0:
            if(list1[0] <= list2[0]):
                merged_list.append(list1.pop(0))
            else:
                merged_list.append(list2.pop(0))
        elif len(list1) > 0:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))

    return merged_list

def main():
    L1 = [1, 3, 5, 7, 8, 9, 10, 10, 15]
    L2 = [0, 2, 2, 6, 10, 11, 13]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
