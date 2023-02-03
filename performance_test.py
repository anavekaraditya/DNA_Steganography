from math import log10, sqrt
import cv2
import numpy as np
from scipy.signal import fftconvolve
from skimage.metrics import structural_similarity as ssim


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def normxcorr2(template, image, mode="valid"):

    # If this happens, it is probably a mistake
    if np.ndim(template) > np.ndim(image) or \
            len([i for i in range(np.ndim(template)) if template.shape[i] > image.shape[i]]) > 0:
        print("normxcorr2: TEMPLATE larger than IMG. Arguments may be swapped.")

    template = template - np.mean(template)
    image = image - np.mean(image)

    a1 = np.ones(template.shape)
    # Faster to flip up down and left right then use fftconvolve instead of scipy's correlate
    ar = np.flipud(np.fliplr(template))
    out = fftconvolve(image, ar.conj(), mode=mode)

    image = fftconvolve(np.square(image), a1, mode=mode) - \
            np.square(fftconvolve(image, a1, mode=mode)) / (np.prod(template.shape))

    # Remove small machine precision errors after subtraction
    image[np.where(image < 0)] = 0

    template = np.sum(np.square(template))
    out = out / np.sqrt(image * template)

    # Remove any divisions by 0 or very close to 0
    out[np.where(np.logical_not(np.isfinite(out)))] = 0

    return out


def main():
    original = cv2.imread("E:/5th Sem/E1-DWS/project/img/3.jpg")
    compressed = cv2.imread("E:/5th Sem/E1-DWS/project/img/test4/3_encrpted.png", 1)
    psnr = PSNR(original, compressed)
    MSE = np.mean((original - compressed) ** 2)
    RMSE = sqrt(MSE)
    SNR = 10 * log10(np.mean(original) / MSE)
    NCC = normxcorr2(original, compressed)
    IF = 1-NCC
    AD = np.mean(original-compressed)
    SSIM = ssim(original, compressed,multichannel=True)
    print(f"1.PSNR value is {psnr} dB")
    print(f"2.MSE value is {MSE} dB")
    print(f"3.RMSE value is {RMSE} dB")
    print(f"4.SNR value is {SNR} dB")
    print(f"5.NCC value is {NCC} ")
    print(f"6.IF value is {IF} ")
    print(f"7.AD value is {AD} ")
    print(f"8.SSIM value is {SSIM} ")


if __name__ == "__main__":
    main()
