import base64

def decode_ascii85(encoded_text):
    # Remove the start and end markers
    encoded_text = encoded_text[2:-2]

    # Decode the ASCII85 encoded text
    decoded_data = base64.a85decode(encoded_text)

    return decoded_data
