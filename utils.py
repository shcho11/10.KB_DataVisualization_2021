출처 : [직딩잇템] 파이썬 시각화 라이브러리로 엑셀 대시보드 만들기(2021-02) 

import xlwings as xw


def percent_to_float(series):
    return series.str.rstrip('%').astype('float')


def rgb_to_int(rgb):
    if isinstance(rgb, str):
        rgb = rgb.lstrip('#')
        if len(rgb) == 3:
            rgb = rgb[0] * 2 + rgb[1] * 2 + rgb[2] * 2
        rgb = int(rgb[:2], 16), int(rgb[2:4], 16), int(rgb[4:], 16)
    return (rgb[2] << 16) + (rgb[1] << 8) + rgb[0]


def right_(range_, step=1):
    row = range_.row
    col = range_.column + step
    return xw.Range((row, col))


def down_(range_, step=1):
    row = range_.row + step
    col = range_.column
    return xw.Range((row, col))
