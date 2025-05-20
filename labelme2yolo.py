import os
import json
from PIL import Image

CLASS_MAP = {"roads": 0}

IMG_DIR = "./images"
JSON_DIR = "./jsons"
OUTPUT_DIR = "./labels"


def check_files():
    json_files = {
        os.path.splitext(f)[0] for f in os.listdir("./jsons") if f.endswith(".json")
    }
    image_files = {
        os.path.splitext(f)[0]
        for f in os.listdir("./images")
        if f.endswith((".jpg", ".png", ".jpeg"))
    }

    if not json_files or not image_files:
        print("错误：jsons 或 images 文件夹为空")
        return False

    json_only = json_files - image_files
    image_only = image_files - json_files

    if json_only:
        print("以下JSON文件缺少对应的图片：", json_only)
    if image_only:
        print("以下图片文件缺少对应的JSON：", image_only)

    return len(json_only) == 0 and len(image_only) == 0


def convert():
    if not os.path.exists(JSON_DIR) or not os.path.exists(IMG_DIR):
        print(f"错误：{JSON_DIR} 或 {IMG_DIR} 文件夹不存在")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not check_files():
        return

    for json_file in os.listdir(JSON_DIR):
        if not json_file.endswith(".json"):
            continue

        json_path = os.path.join(JSON_DIR, json_file)

        # 读取JSON文件
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        image_file = data.get("imagePath")

        # 获取图像大小
        image_path = os.path.join(IMG_DIR, os.path.basename(image_file))
        with Image.open(image_path) as img:
            w, h = img.size

        # 生成输出文件路径
        txt_filename = os.path.splitext(json_file)[0] + ".txt"
        txt_path = os.path.join(OUTPUT_DIR, txt_filename)

        # 写入转换后的标注
        with open(txt_path, "w", encoding="utf-8") as out_file:
            for shape in data["shapes"]:
                label = shape["label"]
                if label not in CLASS_MAP:
                    print(f"警告：未知类别 {label}，跳过")
                    continue

                class_id = CLASS_MAP[label]
                points = shape["points"]

                norm_points = []
                for x, y in points:
                    norm_x = round(x / w, 6)
                    norm_y = round(y / h, 6)
                    norm_points.extend([norm_x, norm_y])

                out_file.write(f"{class_id} " + " ".join(map(str, norm_points)) + "\n")

        print(f"已转换：{json_path} -> {txt_path}")


if __name__ == "__main__":
    convert()