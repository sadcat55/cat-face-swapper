import sys
sys.path.append('lib/pycatfd')
import catfd
from PIL import Image

def main():
        print("Starting to make cat sad!")
        
        input_image = "./images/samples/link.jpg"
        output_path = "."
        use_json = True
        annotate_faces = False
        annotate_landmarks = False
        face_color = [0,0,0]
        landmark_color = [0,0,0]
        save_chip = False

        list_of_cat_faces = catfd.detect(
            input_image, 
            output_path, 
            use_json, 
            annotate_faces,
            annotate_landmarks, 
            face_color, 
            landmark_color, 
            save_chip)

        if len(list_of_cat_faces) > 0:
            for cat_face_info in list_of_cat_faces:

                cat_face = cat_face_info["face"]
                cat_face_position = (cat_face["left"], cat_face["top"])

                sadcat_image = Image.open("./images/sadcat_transparent.png").convert("RGBA")
                sadcat_image = sadcat_image.resize((cat_face["width"],cat_face["height"]))

                target_image = Image.open(input_image).convert("RGBA")
                target_image.alpha_composite(sadcat_image, cat_face_position)
                target_image.save("output.png")
        else:
            print("Could not detect a cat face :(")

main()
