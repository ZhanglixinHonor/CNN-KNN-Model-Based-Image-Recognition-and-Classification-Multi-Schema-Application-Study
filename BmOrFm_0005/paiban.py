import os
from PIL import Image

# 设置文件夹路径和输出图片文件名
folder_path = "E:/Users/zhang/lunwendaima/outputimage"  # 替换为包含图片的文件夹路径
output_image_file = "output_image2.bmp"  # 将输出文件保存为BMP格式

# 获取文件夹中的图片文件列表
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# 指定调整后的图片尺寸
target_width = 300
target_height = 300

# 创建一个新的输出图片
output_width = target_width * 20  # 每行20张图片
output_height = target_height * ((len(image_files) - 1) // 20 + 1)
output_image = Image.new("RGB", (output_width, output_height))

# 拼接图片
x_offset = 0
y_offset = 0
for image_file in image_files:
    image = Image.open(os.path.join(folder_path, image_file))
    # 调整图片尺寸为目标尺寸
    image = image.resize((target_width, target_height))
    output_image.paste(image, (x_offset, y_offset))
    x_offset += target_width
    if x_offset >= output_width:
        x_offset = 0
        y_offset += target_height

# 保存输出图片为BMP格式
output_image.save(output_image_file)

# 显示或输出图片路径
output_image.show()  # 如果你想查看图片
print(f"输出图片已保存到 {output_image_file}")
