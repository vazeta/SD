from pystreamapi import Stream


def print_value(v):
    print(v)


def main():
    array = list(range(10))

    print("Serial execution")
    Stream.of(array).for_each(print_value)

    print("Parallel execution")
    Stream.of(array).parallel().for_each(print_value)


if __name__ == "__main__":
    main()
