import sys
sys.path.append('../pycatfd')
import catfd
from PIL import Image

def main():
        print("Hello world!")
        input_image = "./images/samples/zelda.jpg"
        output_path = "."
        use_json = True
        annotate_faces = False
        annotate_landmarks = False
        face_color = [0,0,0]
        landmark_color = [0,0,0]
        save_chip = True

        list_of_cat_faces = catfd.detect(input_image, output_path, use_json, annotate_faces,
           annotate_landmarks, face_color, landmark_color, save_chip)

        cat_face_info = list_of_cat_faces[0]["face"]
        cat_face_position = (cat_face_info["left"], cat_face_info["top"])

        sadcat_image = Image.open("./images/sadcat-transparent.png").convert("RGBA")
        sadcat_image = sadcat_image.resize((cat_face_info["width"],cat_face_info["height"]))

        target_image = Image.open(input_image).convert("RGBA")
        target_image.alpha_composite(sadcat_image, cat_face_position)
        target_image.save("output.png")


main()
