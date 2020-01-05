import base64
inp = str(input("Text"))
encode_Bytes = base64.b64encode("Riven".encode("utf-8"))
encoded_text = eval("print(str(encode_Bytes,'utf-8'))")
print(encoded_text)