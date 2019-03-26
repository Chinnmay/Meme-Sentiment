import sys
import os
import re
import cv2 

class MemeOCR:
    def __init__(self):
        self._white_thresh = 240
        self._tmp_image_fname = '/tmp/memeocr.jpg'
        self._tmp_txt_base = '/tmp/memeocr'
        self._tmp_txt_fname = self._tmp_txt_base + '.txt'
        self._template_image = None
        self._keep_tmp_files = False

    def set_template(self, fname):
        self._template_image = self._read_image(fname)

    def recognize(self, fname):
        txt = None
        print(fname)
        '''
        im_gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thresh = 127
        im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite('bw_image_bin.png', im_bw)
       	img = self._read_image('bw_image_bin.png')
        '''
        img = self._read_image(fname)
        #print(img)
        self._thresh_words(img, self._template_image)
        print("Inside Recognize")
        self._exec_tesseract()
        txt = self._read_txt()
        self._delete_tmp_files()
        return txt

    def _read_image(self, fname):
        try:
            img = cv2.imread(fname)
        except IOError:
            img = None
        return img

    def _thresh_words(self, img, template):
        if img is None:
            return

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if all([elem >= self._white_thresh for elem in img[i][j]]):
                    img[i][j] = (255, 255, 255)
                else:
                    img[i][j] = (0, 0, 0)

        cv2.imwrite(self._tmp_image_fname, img)

    def _exec_tesseract(self):
        cmd = 'tesseract -l joh %s %s > /dev/null' % (self._tmp_image_fname, self._tmp_txt_base)
        #cmd = 'env TESSDATA_PREFIX=/home/pranny/Desktop/BE Project/meme-sentiment-extraction/controllers/tessdata tesseract -l joh %s %s > /dev/null' % (self._tmp_image_fname, self._tmp_txt_base)
        os.system(cmd)

    def _read_txt(self):
        try:
            fr = open(self._tmp_txt_fname)
        except IOError:
            return None
        content = fr.read()
        fr.close()
        blocks = re.split(r'\n\n', content)
        lines = [re.sub(r'\s+', ' ', block) for block in blocks if block.strip()]
        return lines

    def _delete_tmp_files(self):
        if self._keep_tmp_files:
            return
        if os.path.exists(self._tmp_image_fname):
            os.remove(self._tmp_image_fname)
        if os.path.exists(self._tmp_txt_fname):
            os.remove(self._tmp_txt_fname)

