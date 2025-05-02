import base64

encoded_text = "<~FD,B0+DGm>C3=T>+EV:.+D,>.F*&OGFCfDB+CT.u+EV:.+D,b6+DGm>@<6L4Eb/c)~>"

encoded_text = encoded_text[2:-2]

decoded_data = base64.a85decode(encoded_text)

print(decoded_data)