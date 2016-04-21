#以下来自廖雪峰的Python学习之Python常用第三方模块

#PIL//////////////////////////////////////////////
#PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
#我们可以直接安装使用Pillow。
#操作图像-----------------------------------------------------
#来看看最常见的图像缩放操作，只需三四行代码：
from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

#其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
#比如，模糊效果也只需几行代码：
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')