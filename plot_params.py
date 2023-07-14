import matplotlib.pyplot as plt


def set_plot_params(
    font_family="serif",
    font_weight="heavy",
    label_weight="heavy",
    title_weight="heavy",
    font_size=12,
    legend_fontsize=12,
    math_font="stix",
    xtick_dir="in",
    ytick_dir="in",
    xtick_width=1.5,
    ytick_width=1.5,
    axis_width=1.5,
    xtick_top=False,
    ytick_right=False,
    xtick_minor_visible=False,
    ytick_minor_visible=False,
    xtick_minor_width=1.0,
    ytick_minor_width=1.0,
    xtick_pad=7,
    ytick_pad=7,
    label_pad=10,
    title_pad=10,
    savefig_dpi=300,
    figure_dpi=300,
    savefig_bbox="tight",
):
    """
    该函数用于设置matplotlib绘图参数, 各个参数均为可选参数, 可以在函数调用时进行自定义修改.

    Parameters
    ----------
    font_family : str, optional  字体类型, 默认值为 "serif".
    font_weight : str, optional  字体加粗类型, 默认值为 "heavy".
    label_weight : str, optional  坐标轴标签加粗类型, 默认值为 "heavy".
    title_weight : str, optional  图表标题加粗类型, 默认值为 "heavy".
    font_size : int, optional  字体大小, 默认值为 12.
    legend_fontsize: int, optional  图例字体大小, 默认值为 12.
    math_font : str, optional  数学公式字体类型, 默认值为 "stix", 即斜体.
    xtick_dir : str, optional  x 轴主刻度线方向, 默认值为 "in".
    ytick_dir : str, optional  y 轴主刻度线方向, 默认值为 "in".
    xtick_width : float, optional  x 轴主刻度线宽度, 默认值为 1.5.
    ytick_width : float, optional  y 轴主刻度线宽度, 默认值为 1.5.
    axis_width : float, optional  坐标轴线宽度, 默认值为 1.5.
    xtick_top : bool, optional  是否在 x 轴顶部添加刻度线, 默认值为 False.
    ytick_right : bool, optional  是否在 y 轴右侧添加刻度线, 默认值为 False.
    xtick_minor_visible : bool, optional  是否添加 x 轴次刻度线, 默认值为 False.
    ytick_minor_visible : bool, optional  是否添加 y 轴次刻度线, 默认值为 False.
    xtick_minor_width : float, optional  x 轴次刻度线宽度, 默认值为 1.0.
    ytick_minor_width : float, optional  y 轴次刻度线宽度, 默认值为 1.0.
    xtick_pad : int, optional  x 轴主刻度线标签与刻度线的距离, 默认值为 7.
    ytick_pad : int, optional  y 轴主刻度线标签与刻度线的距离, 默认值为 7.
    label_pad : int, optional  坐标轴标签与坐标轴的距离, 默认值为 10.
    title_pad : int, optional  标题与坐标轴的距离, 默认值为 10.
    savefig_dpi : int, optional  图片保存时的分辨率, 默认值为 300.
    figure_dpi : int, optional  图片显示时的分辨率, 默认值为 300.
    savefig_bbox : str, optional  图片保存时的裁剪方式, 默认值为 "tight", 即裁剪掉图片周围的空白部分.
    -------
    Returns:  None

    其他可以补充的plt.rcParams
    "axes.grid": True/False, 设置是否显示坐标轴网格线.
    "axes.edgecolor": "color", 设置坐标轴边框的颜色.
    "axes.facecolor": "color", 设置坐标轴背景颜色.
    "xtick.labelsize": size, 设置x轴刻度标签的字体大小.
    "ytick.labelsize": size, 设置y轴刻度标签的字体大小.
    "lines.linewidth": width, 设置线条宽度.
    "lines.markersize": size, 设置标记的大小.
    "text.usetex": True/False, 设置是否使用TeX解析字符串中的LaTeX标记.
    "axes.prop_cycle": cycle, 设置默认颜色循环.
    "mathtext.default": 数学公式字体类型, "regular"为非斜体.
    """

    # 创建包含参数名称和对应值的字典
    params = {
        "font.family": font_family,
        "font.weight": font_weight,
        "axes.labelweight": label_weight,
        "axes.titleweight": title_weight,
        "font.size": font_size,
        "legend.fontsize": legend_fontsize,
        "mathtext.fontset": math_font,
        "xtick.direction": xtick_dir,
        "ytick.direction": ytick_dir,
        "xtick.major.width": xtick_width,
        "ytick.major.width": ytick_width,
        "axes.linewidth": axis_width,
        "xtick.top": xtick_top,
        "ytick.right": ytick_right,
        "xtick.minor.visible": xtick_minor_visible,
        "ytick.minor.visible": ytick_minor_visible,
        "xtick.minor.width": xtick_minor_width,
        "ytick.minor.width": ytick_minor_width,
        "xtick.major.pad": xtick_pad,
        "ytick.major.pad": ytick_pad,
        "axes.labelpad": label_pad,
        "axes.titlepad": title_pad,
        "savefig.dpi": savefig_dpi,
        "figure.dpi": figure_dpi,
        "savefig.bbox": savefig_bbox,
    }

    # 将参数设置到 rcParams 中
    plt.rcParams.update(params)
