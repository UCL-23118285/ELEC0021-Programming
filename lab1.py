import sys

def main():
    text = "Hello, World!\n"
    
    if len(sys.argv) < 3:
        print("Usage: python lab1.py --times <number> [--uppercase]")
        sys.exit()
    
    if sys.argv[1] == "--times":
        try:
            times = int(sys.argv[2])
        except ValueError:
            print("Error: --times requires a number")
            sys.exit()

        if times < 1:
            print("Error: --times must be at least 1")
            sys.exit()

        if len(sys.argv) >= 4 and sys.argv[3] == "--uppercase":
            text = text.upper()
        
        print(text * times, end="")


if __name__ == "__main__":
    main()