import base64

def encode_to_base64(text):
    try:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"❌ Error during encoding: {e}"

def decode_from_base64(encoded_text):
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"❌ Error during decoding: {e}"

def main():
    print("===== Base64 Tool by Ayyoub 🔐 =====")
    print("1️⃣  Encode text to Base64")
    print("2️⃣  Decode Base64 to text")
    
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == '1':
        text = input("Enter the text to encode: ")
        result = encode_to_base64(text)
        print(f"\n✅ Encoded Base64:\n{result}")
    
    elif choice == '2':
        encoded_text = input("Enter the Base64 text to decode: ")
        result = decode_from_base64(encoded_text)
        print(f"\n✅ Decoded text:\n{result}")
    
    else:
        print("❌ Invalid choice. Please run the script again and choose 1 or 2.")

if __name__ == "__main__":
    main()
