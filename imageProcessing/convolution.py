import numpy as np

def convolute(im, kernel, padding=False):
    r = int((len(kernel) - 1) / 2)
    out_shape = np.subtract(im.shape, r * 2)
    strided = np.lib.stride_tricks.sliding_window_view(im, kernel.shape)
    tile_kernel = np.tile(kernel, (out_shape[0], out_shape[1], 1, 1))
    out = np.sum(tile_kernel * strided, axis=(2, 3))
    if padding:
        out = np.pad(out, ((0, r), (0, r)))
        out = np.pad(out, ((r, 0), (r, 0)))
    assert out.shape == im.shape, f"{out.shape} is not {im.shape}"
    return out
