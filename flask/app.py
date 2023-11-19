from flask import Flask, render_template, request,jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import io

app = Flask(__name__,static_folder = 'static')


def generate_fake_image(original_image,noise_intensity):            # starGAN接口添加
    image = original_image
    return image

def generate_fake_image_option2(original_image,noise_intensity):        # cycleGAN接口添加
    image = original_image.rotate(180)
    return image

@ app.route('/')                                # 主页
def index():
    return render_template('index.html')

@ app.route('/about')                       # 项目简介
def about():
    return render_template('introduction.html')

@app.route('/test')             # 测试界面
def test():
    return render_template('test.html')

@app.route('/result', methods=['POST'])          # 结果展示界面
def result():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    noise_intensity = int(request.form['noise_intensity'])
    selected_option = request.form['selected_option']

    if file:
        original_image = Image.open(file)
        if selected_option == 'option1':
            fake_image = generate_fake_image(original_image, noise_intensity)
        elif selected_option == 'option2':
            fake_image = generate_fake_image_option2(original_image,noise_intensity)
        else:
            # Handle the case where no option is selected
            return render_template('index.html', error='Invalid option selected')

        static_folder = 'static'
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)

        fake_image_path = os.path.join(static_folder, 'fake_image.jpg')
        fake_image.save(fake_image_path)
        original_image_path = os.path.join(static_folder,'original_image.jpg')
        original_image.save(original_image_path)
        
        return render_template('result.html', original_image=original_image, 
                               fake_image_path=fake_image_path,fake_image = fake_image
                                ,noise_intensity=noise_intensity)
        
@app.route('/result2', methods=['GET'])         # 输出对比图
def result2():
    return render_template("result2.html")


if __name__ == '__main__':
    app.run(debug = True)
