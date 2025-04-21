from pponnxcr import TextSystem
import cv2,os

#print(os.listdir(r"D:\System-Games\AnJianJingLingMobileHelper\按键精灵手机助手\Script\Fate-Grand-Order-AnJianJingLing-Script\pic4scripts"))

ZHS = TextSystem('zhs')
ZHT = TextSystem('zht')
JA = TextSystem('ja')
EN = TextSystem('en')

img = cv2.imread('30np.png')
#img = cv2.imread("D:\\System-Games\\AnJianJingLingMobileHelper\\按键精灵手机助手\\Script\\Fate-Grand-Order-AnJianJingLing-Script\\pic4scripts\\30np.png")
print(img)
cv2.imshow('displaymywindows', img)
cv2.waitKey(0)   #wait for a keyboard input
cv2.destroyAllWindows()
#ZHS.ocr_single_line(img)
#ZHS.ocr_lines([img, ...])
#ZHS.detect_and_ocr(img)

br = EN.ocr_single_line(img)[0]
print(br)
# def getFieldServantNp(self,pos):return self._ocrInt((220+317*pos,655,271+317*pos,680)) # 1280*720

"""
logger=getLogger('Ocr')
class Ocr(TextSystem):
    @logit(logger)
    def __call__(self,img):return super().ocr_single_line(img)[0]
    def ocrInt(self,img):return int('0'+''.join(i for i in self(img)if i.isdigit()))
    def ocrText(self,img):return self(img)
    @logit(logger,transform=lambda x:'|'.join(x))
    def ocrArea(self,img):return[i.text for i in self.detect_and_ocr(img)]
 """