#!/usr/bin/env python3


def spam_detection(random_state=0, fraction=1.0):
    return 0.0, 0, 0

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
