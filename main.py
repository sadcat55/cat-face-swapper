import sys
sys.path.append('../pycatfd')
import catfd
from PIL import Image

def main():
	print("Hello world!")
	input_image = "./images/samples/nero.jpg"
	output_path = "."
	use_json = True
	annotate_faces = False
	annotate_landmarks = False
	face_color = [0,0,0]
	landmark_color = [0,0,0]
	save_chip = True

	#list_of_cat_faces = catfd.detect(input_image, output_path, use_json, annotate_faces,
	#   annotate_landmarks, face_color, landmark_color, save_chip)

	sadcat_image = Image.open("./images/sadcat-transparent.png").convert("RGBA")
	target_image = Image.open(input_image).convert("RGBA")
	target_image.alpha_composite(sadcat_image)
	target_image.save("output.png")


main()
