# Pixel-Art
Generates a pixel art image out of a regular image. 

The resultant pixelated images can be found in the main folder, and the scripts used to create them can be found in the scripts subfolder.

The BuiltIn script uses the builtin resize command within the Pillow library to generate the final pixel image.

The Average script finds the average value from every pixel within a given block and uses that to generate the pixelated image. 

The Mode script finds the most common pixel value from set of all pixels within a given block and uses that to generate the pixelated image. 
Because, it completely neglects all color values that aren't the most prominent this script tends to not effectively capture smaller details, such as the stem in the example photo of an apple.
