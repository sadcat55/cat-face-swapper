import sys
sys.path.append('lib/pycatfd')

import catfd
from PIL import Image

from os import listdir, makedirs
from os.path import isfile, join, exists, basename, splitext

from math import atan2, degrees

def swap_cat_face_with_sad_cat_face(input_image_path, output_folder_path):
    use_json = True
    annotate_faces = False
    annotate_landmarks = False
    face_color = [0,0,0]
    landmark_color = [0,0,0]
    save_chip = False

    list_of_cat_faces = catfd.detect(
        input_image_path, 
        output_folder_path, 
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
            cat_face_landmarks = cat_face["landmarks"]

            sadcat_image = Image.open("./images/sadcat_transparent.png").convert("RGBA")
            sadcat_image = sadcat_image.resize((cat_face["width"],cat_face["height"]))

            rotation_degree = -get_angle_of_line_of_two_points(cat_face_landmarks["Left Eye"], cat_face_landmarks["Right Eye"])
            sadcat_image = sadcat_image.rotate(rotation_degree)
            print("Rotate sad cat by " + str(rotation_degree) + " degrees")

            target_image = Image.open(input_image_path).convert("RGBA")
            target_image.alpha_composite(sadcat_image, cat_face_position)
            target_image_file_name, extension = splitext(basename(input_image_path))

            output_image_path = join(output_folder_path, target_image_file_name + '.png')
            print('Creating sad cat: ' + output_image_path)
            target_image.save(output_image_path)
    else:
        print("Could not detect a cat face :(")    

def get_angle_of_line_of_two_points(p1_tuple=(0,0), p2_tuple=(0,0)):
    x_diff = p2_tuple[0] - p1_tuple[0]
    y_diff = p2_tuple[1] - p1_tuple[1]
    return degrees(atan2(y_diff, x_diff))

def main():
    print("Starting to make cat sad!")
    input_folder_path = './happy_cat_inputs'
    output_folder_path = './sad_cat_outputs'

    if not exists(input_folder_path):
        print('Could not find input folder with happy cats.')
        exit(1)

    if not exists(output_folder_path):
        print('Creating output folder path.')
        makedirs(output_folder_path)

    happy_cat_image_paths = [join(input_folder_path, file_name) for file_name in listdir(input_folder_path) if isfile(join(input_folder_path, file_name))]

    print(happy_cat_image_paths)

    for happy_cat_image_path in happy_cat_image_paths:
        swap_cat_face_with_sad_cat_face(happy_cat_image_path, output_folder_path)
        
    

main()
