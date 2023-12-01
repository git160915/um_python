text = "X-DSPAM-Confidence:    0.8475"
index = text.find(":")
num = text[index+1:].strip()
num_float = 0.0

try :
    num_float = float(num)
except :
    print("error converting", num)

print(num_float)