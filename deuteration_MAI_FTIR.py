import maat as mt
from math import sqrt


'''
Tool to analyze MAI deuteration with ATR data.\n
Working on vMT.1.0.0
'''


atr = mt.Spectra(
    type='ATR',
    title=None,
    save_as=None,
    filename=[
        'data/FTIR/MAI_comGCSM_ATR_ISIS_256scans_4cm-res_atr-corrected.dat',
        'data/FTIR/MAI-ND_KS169_ATR_ISIS_256scans_4cm-res_atr-corrected.dat'
        ],
    units_in=['cm-1'],
    units='cm-1',
    plotting=mt.Plotting(
        low_xlim=None,
        top_xlim=None,
        low_ylim=None,
        top_ylim=None,
        figsize=None,
        offset=True,
        log_xscale=False,
        normalize=False,
        show_yticks=False,
        legend=['MAI', 'MAI-ND-03']
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )

ymin_NH = 0.25
ymax_NH = 0.703
ymin_ND = 0.021
ymax_ND = 0.184

plateau_NH = [3340, 4000]
plateau_ND = [3260, 4000]

peak_C =[2950, 2976]
peak_NH = [2920, 3320]

atr.scale_range.ymin = [ymin_NH, ymin_ND]
atr.scale_range.ymax = [ymax_NH, ymax_ND]

atr = mt.tools.normalize(atr)

baseline_H, baseline_H_error = mt.fit.plateau(atr, plateau_NH, 0)
baseline_D, baseline_D_error = mt.fit.plateau(atr, plateau_ND, 1)

baseline_C, baseline_C_error = baseline_D, baseline_D_error

area_C, area_error_C = mt.fit.area_under_peak(atr, [peak_C[0], peak_C[1], baseline_C, baseline_C_error], 1)
area_NH, area_NH_error = mt.fit.area_under_peak(atr, [peak_NH[0], peak_NH[1], baseline_H, baseline_H_error], 0)
area_ND, area_ND_error = mt.fit.area_under_peak(atr, [peak_NH[0], peak_NH[1], baseline_D, baseline_D_error], 1)

area_NH = area_NH - area_C
area_ND = area_ND - area_C

area_NH_error = sqrt(area_NH_error**2 + area_error_C**2)
area_ND_error = sqrt(area_ND_error**2 + area_error_C**2)

deuteration = (area_NH - area_ND) / area_NH
deuteration_error = sqrt((sqrt(area_NH_error**2 + area_ND_error**2) / (area_NH - area_ND))**2 + (area_NH_error / area_NH)**2)


print(f'MAI deuteration: {deuteration:.2f} ± {deuteration_error:.2f}')
print(area_NH)
print(area_NH_error)
print(baseline_error_C)

mt.plot.spectra(atr)

