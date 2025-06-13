text = "   HELLO     woRld!    "
print(text.strip())
print(text.replace(" ", ""))
print(text.lower())
print(text.replace(" ", "").lower())
print(text.split())
print(text.title())
print(text.title().split())
print(' '.join(text.split()).lower())

str = text.replace(" ", "").lower()
print(list(str))


char_list = [ch for ch in text if ch != ' ']
print(char_list)