from rembg import remove
from PIL import Image


input_path = "rayan.jpg"
output_path = "output.jpg"

with open(input_path , "rb") as i:
    with open(output_path , "wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)