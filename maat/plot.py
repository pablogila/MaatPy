from .core import *
from .operations import normalize


def spectra(spectrum:Spectra):

    sdata = deepcopy(spectrum)
    scale_factor = sdata.plotting.scale_factor if sdata.plotting.scale_factor else 1.0

    fig, ax = plt.subplots()
    if sdata.plotting.figsize:
        fig, ax = plt.subplots(figsize=sdata.plotting.figsize)

    if sdata.plotting.normalize is True:
        sdata = normalize(sdata)
    normalized_dataframes = sdata.dataframe

    all_y_values = []
    for df in normalized_dataframes:
        df_trim = df
        if sdata.plotting.low_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] >= sdata.plotting.low_xlim)]
        if sdata.plotting.top_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] <= sdata.plotting.top_xlim)]
        all_y_values.extend(df_trim[df_trim.columns[1]].tolist())
    calculated_low_ylim = min(all_y_values)
    calculated_top_ylim = max(all_y_values) * scale_factor

    ymax_on_range = None
    if sdata.scale_range is not None:
        df_index = sdata.scale_range.index if sdata.scale_range.index else 0
        df0 = sdata.dataframe[df_index]
        if sdata.scale_range.xmin :
            df0 = df0[(df0[df0.columns[0]] >= sdata.scale_range.xmin)]
        if sdata.scale_range.xmax:
            df0 = df0[(df0[df0.columns[0]] <= sdata.scale_range.xmax)]
        ymax_on_range = df0[df0.columns[1]].max()
    if sdata.plotting.zoom_range and ymax_on_range is not None:
        calculated_top_ylim = ymax_on_range * scale_factor

    if sdata.plotting.low_ylim is None:
        sdata.plotting.low_ylim = calculated_low_ylim
    if sdata.plotting.top_ylim is None:
        sdata.plotting.top_ylim = calculated_top_ylim
    low_ylim = sdata.plotting.low_ylim
    top_ylim = sdata.plotting.top_ylim

    ###########  ME LLEGO POR AQUI

    for df, name in zip(sdata.dataframe, sdata.filename):
        if sdata.plotting.offset is True:# and (sdata.low_ylim is not None) and (sdata.top_ylim is not None):
            number_of_plots = len(sdata.dataframe)
            height = top_ylim - low_ylim
            reverse_index = (number_of_plots - 1) - sdata.filename.index(name)
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (reverse_index * height) / number_of_plots
            #df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (sdata.filename.index(name) * height) / number_of_plots

        strings_to_delete_from_name = ['.csv', '_INS', '_ATR', '_FTIR', '_temp', '_RAMAN', '_Raman']
        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if sdata.plotting.legend and isinstance(sdata.plotting.legend, list):
            name_clean = sdata.plotting.legend[sdata.filename.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    if sdata.plotting.low_xlim is not None:
        ax.set_xlim(left=sdata.plotting.low_xlim)
    if sdata.plotting.top_xlim is not None:
        ax.set_xlim(right=sdata.plotting.top_xlim)
    if sdata.plotting.low_ylim is not None:
        ax.set_ylim(bottom=sdata.plotting.low_ylim)
    if sdata.plotting.top_ylim is not None:
        ax.set_ylim(top=sdata.plotting.top_ylim)

    plt.title(sdata.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if sdata.plotting.log_xscale:
        ax.set_xscale('log')
    if not sdata.plotting.show_yticks:
        ax.set_yticks([])
    if sdata.plotting.legend is not False:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if sdata.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, sdata.save_as)
        plt.savefig(save_name)
    
    plt.show()

