import base64

# Ask the user to enter the Base64-encoded string
base64_input = input("Enter the Base64-encoded text: ")

try:
    # Decode the Base64 input
    decoded_bytes = base64.b64decode(base64_input)
    decoded_text = decoded_bytes.decode('utf-8')
    
    print("Decoded text:")
    print(decoded_text)

except Exception as e:
    print("An error occurred during decoding:")
    print(e)
