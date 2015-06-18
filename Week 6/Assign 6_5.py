text = "X-DSPAM-Confidence:    0.8475";

atcolon = text.find(":")

num = float(text[atcolon+1:])
print num