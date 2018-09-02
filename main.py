import sys
sys.path.append('../pycatfd')
import catfd

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
	catfd.detect(input_image, output_path, use_json, annotate_faces,
	   annotate_landmarks, face_color, landmark_color, save_chip)

main()
