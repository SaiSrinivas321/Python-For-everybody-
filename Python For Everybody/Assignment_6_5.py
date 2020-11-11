text = "X-DSPAM-Confidence:    0.8475";
ssp=text.find("0");

print(float(text[ssp:]))
