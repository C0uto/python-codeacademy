import base64

def decode_ascii85(encoded_text):
    # Remove the start and end markers
    text_with_nomarkers = encoded_text[2:-2]

    # Decode the ASCII85 encoded text
    decoded_data = base64.a85decode(text_with_nomarkers)

    return decoded_data
