import matplotlib.pyplot as plt


def set_plot_params(
    font_family="serif",
    font_weight="heavy",
    axes_labelweight="heavy",
    axes_titleweight="heavy",
    font_size=12,
    legend_fontsize=12,
    mathtext_fontset="stix",
    xtick_direction="in",
    ytick_direction="in",
    xtick_major_width=1.5,
    ytick_major_width=1.5,
    axes_linewidth=1.5,
    xtick_top=False,
    ytick_right=False,
    xtick_minor_visible=False,
    ytick_minor_visible=False,
    xtick_minor_width=1.0,
    ytick_minor_width=1.0,
    xtick_major_pad=7,
    ytick_major_pad=7,
    axes_labelpad=10,
    axes_titlepad=10,
    savefig_dpi=300,
    figure_dpi=300,
    savefig_bbox="tight",
):
    """
    设置matplotlib绘图参数.

    Args:
        font_family (str, optional): 字体类型. Defaults to "serif".
        font_weight (str, optional): 字体加粗类型. Defaults to "heavy".
        axes_labelweight (str, optional): 坐标轴标签加粗类型. Defaults to "heavy".
        axes_titleweight (str, optional): 图表标题加粗类型. Defaults to "heavy".
        font_size (int, optional): 字体大小. Defaults to 12.
        legend_fontsize (int, optional): 图例字体大小. Defaults to 12.
        mathtext_fontset (str, optional): 数学公式字体类型. Defaults to "stix".
        xtick_direction (str, optional): x 轴主刻度线方向. Defaults to "in".
        ytick_direction (str, optional): y 轴主刻度线方向. Defaults to "in".
        xtick_major_width (float, optional): x 轴主刻度线宽度. Defaults to 1.5.
        ytick_major_width (float, optional): y 轴主刻度线宽度. Defaults to 1.5.
        axes_linewidth (float, optional): 坐标轴线宽度. Defaults to 1.5.
        xtick_top (bool, optional): 是否在 x 轴顶部添加刻度线. Defaults to False.
        ytick_right (bool, optional): 是否在 y 轴顶部添加刻度线. Defaults to False.
        xtick_minor_visible (bool, optional): 是否添加 x 轴次刻度线. Defaults to False.
        ytick_minor_visible (bool, optional): 是否添加 y 轴次刻度线. Defaults to False.
        xtick_minor_width (float, optional): x 轴次刻度线宽度. Defaults to 1.0.
        ytick_minor_width (float, optional): y 轴次刻度线宽度. Defaults to 1.0.
        xtick_major_pad (int, optional): x 轴主刻度线标签与刻度线的距离. Defaults to 7.
        ytick_major_pad (int, optional): y 轴主刻度线标签与刻度线的距离. Defaults to 7.
        axes_labelpad (int, optional): 坐标轴标签与坐标轴的距离. Defaults to 10.
        axes_titlepad (int, optional): 标题与坐标轴的距离. Defaults to 10.
        savefig_dpi (int, optional): 图片保存时的分辨率. Defaults to 300.
        figure_dpi (int, optional): 图片显示时的分辨率. Defaults to 300.
        savefig_bbox (str, optional): 图片保存时的裁剪方式, "tight"表示裁剪掉图片周围的空白部分. Defaults to "tight".

    Returns:
        dict: matplotlib绘图参数dict.

   -------

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
        "axes.labelweight": axes_labelweight,
        "axes.titleweight": axes_titleweight,
        "font.size": font_size,
        "legend.fontsize": legend_fontsize,
        "mathtext.fontset": mathtext_fontset,
        "xtick.direction": xtick_direction,
        "ytick.direction": ytick_direction,
        "xtick.major.width": xtick_major_width,
        "ytick.major.width": ytick_major_width,
        "axes.linewidth": axes_linewidth,
        "xtick.top": xtick_top,
        "ytick.right": ytick_right,
        "xtick.minor.visible": xtick_minor_visible,
        "ytick.minor.visible": ytick_minor_visible,
        "xtick.minor.width": xtick_minor_width,
        "ytick.minor.width": ytick_minor_width,
        "xtick.major.pad": xtick_major_pad,
        "ytick.major.pad": ytick_major_pad,
        "axes.labelpad": axes_labelpad,
        "axes.titlepad": axes_titlepad,
        "savefig.dpi": savefig_dpi,
        "figure.dpi": figure_dpi,
        "savefig.bbox": savefig_bbox,
    }

    # 将参数设置到 rcParams 中
    plt.rcParams.update(params)

    return params


def set_roman_plot_params(**kwargs):
    """
    设置matplotlib的字体为Times New Roman.

    **kwargs: 可选参数, 与set_plot_params中的参数相同.
    """

    params = set_plot_params(**kwargs)

    params["font.family"] = "sans-serif"
    params["font.sans-serif"] = ["Times New Roman"]

    plt.rcParams.update(params)
