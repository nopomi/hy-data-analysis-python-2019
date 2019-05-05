#!/usr/bin/env python3

def merge(L1, L2):
    list1 = L1.copy()
    list2 = L2.copy()
    merged_list = []
    while True:
        if (not list1) and (not list2):
            break;
        elif not list1:
            merged_list.append(list2.pop(0))
        elif not list2:
            merged_list.append(list1.pop(0))
        else:
            if(list1[0] <= list2[0]):
                merged_list.append(list1.pop(0))
            elif(list1[0] > list2[0]):
                merged_list.append(list2.pop(0))

    return merged_list

def main():
    pass

if __name__ == "__main__":
    main()
