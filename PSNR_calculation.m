function PSNR = PSNR_calculation(MSE)
    PSNR = 10 * log10 (1 / MSE);