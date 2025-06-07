# test_runner.py

def symbolic_echo(input_text):
    echo_prefix = "🌀 ECHO RECEIVED: "
    return f"{echo_prefix}{input_text.strip()}"

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()
        output = symbolic_echo(input_text)
        print(output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
