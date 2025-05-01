import base64



def decode_text(text):
    try:
        decoded_bytes = base64.b64decode(text.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        return f"Failed to decode: {e}"

def main():
    text = input("Enter Base64 string to decode: ")
    decoded = decode_text(text)
    print(f"\nDecoded : {decoded}")

if __name__ == "__main__":
    main()
