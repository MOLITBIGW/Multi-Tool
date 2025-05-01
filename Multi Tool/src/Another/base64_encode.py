import base64
import os


def encode_text(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def main():
    text = input("Enter text to encode: ")
    encoded = encode_text(text)
    print(f"\nEncoded : {encoded}")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
