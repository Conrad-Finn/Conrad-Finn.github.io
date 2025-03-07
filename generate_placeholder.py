from PIL import Image, ImageDraw, ImageFont
import os

def create_emotion_coach_image():
    # 创建一个300x250的图片，使用渐变背景
    width = 300
    height = 250
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # 创建渐变背景
    for y in range(height):
        r = int(26 + (159 - 26) * y / height)
        g = int(159 + (255 - 159) * y / height)
        b = int(255 + (255 - 255) * y / height)
        for x in range(width):
            draw.point((x, y), fill=(r, g, b))
    
    # 绘制模拟的界面元素
    # 对话框背景
    draw.rectangle([20, 20, 280, 230], fill=(255, 255, 255, 128), outline=(255, 255, 255), width=2)
    
    # 绘制表情符号
    emojis = ["😊", "😢", "😡", "😌"]
    for i, emoji in enumerate(emojis):
        x = 40 + i * 60
        draw.text((x, 40), emoji, fill=(255, 255, 255), font=None, size=20)
    
    # 绘制文本框
    draw.rectangle([30, 100, 270, 150], fill=(255, 255, 255, 64), outline=(255, 255, 255))
    draw.text((40, 115), "分析您的情绪状态...", fill=(255, 255, 255), font=None)
    
    # 绘制按钮
    draw.rectangle([100, 180, 200, 210], fill=(78, 124, 255), outline=(255, 255, 255))
    draw.text((120, 190), "开始分析", fill=(255, 255, 255), font=None)
    
    # 保存图片
    if not os.path.exists('images'):
        os.makedirs('images')
    image.save('images/emotion-coach.png')

if __name__ == "__main__":
    create_emotion_coach_image() 