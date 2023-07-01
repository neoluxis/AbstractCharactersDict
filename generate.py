from PIL import Image, ImageDraw, ImageFont
import os

def rmdir(path):
    try:
        ls = os.listdir(path)
    except FileNotFoundError:
        print("File not found! ")
        return
    for i in ls:
        fp = os.path.join(path, i)
        print(f'Deleting {fp}')
        if os.path.isdir(fp):
            rmdir(fp)
        else:
            os.remove(fp)

class Font:
    def __init__(self, path, size=650, ypos=490):
        self.path = path
        self.size = size
        self.ypos = ypos

    def genFont(self):
        return ImageFont.truetype(self.path, self.size)

class Pic:
    def __init__(self, path, font, char):
        self.path = path
        self.font = font
        self.char = char

    def generate(self):
        image = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((10, 10, 990, 990), outline='black', fill='white', width=30)
        draw.ellipse((80, 80, 920, 920), outline='black', fill='white', width=60)
        draw.text((500, self.font.ypos), self.char, fill='black', anchor='mm', font=self.font.genFont())
    #    image.resize((100, 100), Image.LANCZOS).save(
    #    f'small/{i:04d}_{letter}.png')  # for emoji
        image.resize((512, 512), Image.LANCZOS).save(
        f'large/{self.path}.png')  # for sticker


LETTERS = '典孝急乐麻批蚌绷盒赢输对退寄创绝谔鼠兔神友躺卷润狂图了献忠支洼爆死歇反共中美日韩党雅俗佛草逼冲浪汗包子习毛偷傻善编恰哈拉摇晶哥粪钓灵车软硬抄爬原马唉资本我爹爷拳牛'

# LETTERS = '老田NB'

#FONT = Font('繁简篆书.ttf')
FONT = Font('三极隶书简体.ttf', ypos=420)

#FONT = ImageFont.truetype('三极隶书简体.ttf', 650)

rmdir('small')
rmdir('large')

print('旧文件清理完成')

os.makedirs('small', exist_ok=True)
os.makedirs('large', exist_ok=True)

i = 0
for letter in LETTERS:
    img = f'{i:04d}_{letter}'
    print(img)
    i += 1
    t = Pic(font=FONT, path=img, char=letter)
    t.generate()

