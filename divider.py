import os
import random
import shutil

# 设置随机种子确保可重复性
random.seed(42)

IMG_DIR = "./images"
LABEL_DIR = "./labels"

TRAIN_IMG_DIR = "./dataset/images/train"
TRAIN_LABEL_DIR = "./dataset/labels/train"
VAL_IMG_DIR = "./dataset/images/val"
VAL_LABEL_DIR = "./dataset/labels/val"

def divide_dataset():
    os.makedirs(TRAIN_IMG_DIR, exist_ok=True)
    os.makedirs(TRAIN_LABEL_DIR, exist_ok=True)
    os.makedirs(VAL_IMG_DIR, exist_ok=True)
    os.makedirs(VAL_LABEL_DIR, exist_ok=True)

    all_images = [f for f in os.listdir(IMG_DIR) if f.endswith(".jpg")]
    num_val = int(len(all_images) * 0.2)  # 20%用于验证集
    
    val_images = random.sample(all_images, num_val)
    train_images = [img for img in all_images if img not in val_images]
    
    # 训练集
    for img_name in train_images:
        src_img = os.path.join(IMG_DIR, img_name)
        dst_img = os.path.join(TRAIN_IMG_DIR, img_name)
        shutil.copy2(src_img, dst_img)
    
        label_name = os.path.splitext(img_name)[0] + ".txt"
        src_label = os.path.join(LABEL_DIR, label_name)
        dst_label = os.path.join(TRAIN_LABEL_DIR, label_name)
        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)
    
    # 验证集
    for img_name in val_images:
        src_img = os.path.join(IMG_DIR, img_name)
        dst_img = os.path.join(VAL_IMG_DIR, img_name)
        shutil.copy2(src_img, dst_img)
    
        label_name = os.path.splitext(img_name)[0] + ".txt"
        src_label = os.path.join(LABEL_DIR, label_name)
        dst_label = os.path.join(VAL_LABEL_DIR, label_name)
        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)
    
    print(f"成功复制 {len(train_images)} 个文件到训练集")
    print(f"成功复制 {len(val_images)} 个文件到验证集")
    
if __name__ == "__main__":
    divide_dataset()