import os


IMG_DIR = "./images"
LABEL_DIR = "./labels"


def genereate_neg_samples():
    os.makedirs(LABEL_DIR, exist_ok=True)

    img_files = [
        f for f in os.listdir(IMG_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    count = 0
    for img_file in img_files:
        txt_name = os.path.splitext(img_file)[0] + ".txt"
        txt_path = os.path.join(LABEL_DIR, txt_name)

        if not os.path.exists(txt_path):
            open(txt_path, "w").close()
            count += 1

    print(f"生成 {count} 个负样本")


if __name__ == "__main__":
    genereate_neg_samples()
