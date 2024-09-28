import pyperclip
offset = input("どこからの記述かを入力(offset): 0x")
reg = input("使用するレジスタを記入(0-F):")
mode = input("可読性を下げて行数短縮する場合[y]を入力:")
print("クリップボードにhexソースをコピーしたらエンター")
input()
code = ""
lines = pyperclip.paste().split('\n')
if mode == "y":
    for i in range(int(len(lines)/2)):
        code = f'{code}080{reg}0000 {int(offset.lstrip("0"),16) + 8*i:08X} {lines[2*i+1]} {lines[2*i]}\n'
    if len(lines)%2 == 1:
        code = f'{code}040{reg}0000 {int(offset.lstrip("0"),16) + 4*(len(lines)-1):08X} {lines[len(lines)-1]}\n'
else:
    for i in range(int(len(lines))):
        code = f'{code}\n040{reg}0000 {int(offset.lstrip("0"),16) + 4*i:08X} {lines[i]}\n'
pyperclip.copy(code)
print(code)