# ascii image renderer

from PIL import Image
import numpy as np

# light to dark ascii characters for brightness
monochrome_ascii = [' ', '.', ':', '=', '+', '*', '#', '%', '@']

# be careful when adjusting w and h the aspect ratio needs to be 2 (since notepad text is around 2:1 w:h)
def im_to_array(path, w=200, h=100):
    with Image.open(path) as path_im:
        path_im = path_im.convert('L')

        path_im = path_im.resize((w, h))

        im_data = np.array(path_im)

        return im_data

# based on brightness of pixels 0-255 creates an array with an ascii characters
def ascii_array(path):
    im_data = im_to_array(path)

    ascii_matrix = []

    for im_row in im_data:

        cur_ascii_row = []
        for cur_brightness in im_row:

            if 0 <= cur_brightness <= 27:
                cur_ascii_row.append(monochrome_ascii[8])
            elif 28 <= cur_brightness <= 55:
                cur_ascii_row.append(monochrome_ascii[7])
            elif 56 <= cur_brightness <= 83:
                cur_ascii_row.append(monochrome_ascii[6])
            elif 84 <= cur_brightness <= 111:
                cur_ascii_row.append(monochrome_ascii[5])
            elif 112 <= cur_brightness <= 139:
                cur_ascii_row.append(monochrome_ascii[4])
            elif 140 <= cur_brightness <= 167:
                cur_ascii_row.append(monochrome_ascii[3])
            elif 168 <= cur_brightness <= 195:
                cur_ascii_row.append(monochrome_ascii[2])
            elif 196 <= cur_brightness <= 223:
                cur_ascii_row.append(monochrome_ascii[1])
            elif 224 <= cur_brightness <= 255:
                cur_ascii_row.append(monochrome_ascii[0])

        ascii_matrix.append(cur_ascii_row)

    return ascii_matrix


def ascii_arr_tostr(ascii_array, txtfile):
    ascii_s = ''

    for ascii_row in ascii_array:
        for ascii_ch in ascii_row:
            ascii_s += ascii_ch
        ascii_s += '\n'


    ascii_txt = open(txtfile, 'x')
    ascii_txt.write(ascii_s)
    ascii_txt.close()


# function u use to make ascii images lol
def im_to_ascii(pathname, saveas=None):

    if saveas == None:
        pathname_wo_ext = ''
        for ch in pathname:
            if ch == '.':
                break
            pathname_wo_ext += ch

        saveas = pathname_wo_ext + '.txt'

    ascii_data = ascii_array(pathname)
    ascii_arr_tostr(ascii_data, saveas)














