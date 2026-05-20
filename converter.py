def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_hex(n):
    return hex(n)[2:].upper()

def decimal_to_octal(n):
    return oct(n)[2:]

def to_decimal(value, base):
    return int(value, base)

def display_all(decimal):
    print("\n" + "="*40)
    print(f"  Decimal     : {decimal}")
    print(f"  Binary      : {decimal_to_binary(decimal)}")
    print(f"  Hexadecimal : {decimal_to_hex(decimal)}")
    print(f"  Octal       : {decimal_to_octal(decimal)}")
    print("="*40 + "\n")

def main():
    print("\n" + "="*40)
    print("   🔢 Number Systems Converter")
    print("="*40)

    while True:
        print("\n  [1] Decimal → All")
        print("  [2] Binary → Decimal")
        print("  [3] Hexadecimal → Decimal")
        print("  [4] Octal → Decimal")
        print("  [5] Quit")

        choice = input("\n  Choose an option: ").strip()

        if choice == '5':
            print("\n  Goodbye! 👋\n")
            break

        elif choice == '1':
            try:
                n = int(input("  Enter decimal number: ").strip())
                if n < 0:
                    print("  ❌ Please enter a positive number.")
                    continue
                display_all(n)
            except ValueError:
                print("  ❌ Invalid number.")

        elif choice == '2':
            try:
                val = input("  Enter binary number (e.g. 1010): ").strip()
                result = to_decimal(val, 2)
                print(f"\n  ✅ Decimal: {result}")
                display_all(result)
            except ValueError:
                print("  ❌ Invalid binary number.")

        elif choice == '3':
            try:
                val = input("  Enter hex number (e.g. 1F): ").strip()
                result = to_decimal(val, 16)
                print(f"\n  ✅ Decimal: {result}")
                display_all(result)
            except ValueError:
                print("  ❌ Invalid hexadecimal number.")

        elif choice == '4':
            try:
                val = input("  Enter octal number (e.g. 17): ").strip()
                result = to_decimal(val, 8)
                print(f"\n  ✅ Decimal: {result}")
                display_all(result)
            except ValueError:
                print("  ❌ Invalid octal number.")

        else:
            print("  ❌ Invalid option. Choose 1 to 5.")

if __name__ == "__main__":
    main()
