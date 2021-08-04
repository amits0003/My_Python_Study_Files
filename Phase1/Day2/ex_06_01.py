text = "X-DSPAM-Confidence:    0.8475"

dot_pos = text.find('.')

number = text[dot_pos:]

float_num = float(number)

print(float_num)