import json
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import TwoSlopeNorm, LinearSegmentedColormap

table4 = json.load(open('mapdata/table4_data.json', encoding='utf-8'))
# order: [genCPI_S1,S2,S3, realHHC_S1,S2,S3, realGDP_S1,S2,S3, adjHHC_S1,S2,S3]

foodCPI = {
"NAD": [8.962212, 6.567348, -0.526175], "SumUt": [6.847401, 5.297776, -1.365807],
"SumBar": [6.957204, 5.357065, -1.351866], "RiauProv": [6.213796, 4.864033, -1.630095],
"KepRi": [5.386530, 4.248023, -2.023384], "Jambi": [6.809727, 5.161987, -1.516020],
"SumSel": [5.539773, 4.391947, -2.071485], "BaBel": [6.016424, 4.763034, -1.720803],
"Bengkulu": [6.001621, 4.737143, -1.831743], "Lampung": [5.690924, 4.475426, -2.134392],
"DKI": [5.249028, 4.215250, -2.156351], "JaBar": [5.299058, 4.212009, -2.114463],
"Banten": [5.346482, 4.260541, -2.133702], "JaTeng": [6.023199, 4.712000, -2.082866],
"DIY": [6.545387, 5.060851, -1.797307], "JaTim": [5.422487, 4.253477, -2.430859],
"KalBar": [6.282167, 4.953879, -1.653861], "KalTeng": [5.537592, 4.378411, -2.045899],
"KalSel": [5.640488, 4.484859, -2.109900], "KalTim": [5.297140, 4.193938, -2.207529],
"KalUt": [5.219862, 4.125732, -2.288445], "SulUt": [5.642787, 4.484869, -2.112405],
"Gorontalo": [6.289515, 5.002404, -1.646641], "SulTeng": [6.008323, 4.796933, -1.842788],
"SulaSel": [5.705435, 4.553928, -2.199712], "SulBar": [5.719409, 4.521653, -2.174608],
"SulTra": [6.319229, 5.029347, -1.677247], "Bali": [5.757492, 4.509308, -2.161990],
"NTB": [7.072178, 5.538476, -1.382861], "NTT": [7.809688, 6.224201, -0.631751],
"Maluku": [7.379317, 5.749669, -1.057188], "MalUt": [6.329913, 5.045629, -1.490531],
"PapuaBar": [6.200365, 4.903418, -1.637489], "PapuaProv": [5.852525, 4.649023, -1.779709],
}

name_to_abbr = {
    "Aceh": "NAD", "Sumatera Utara": "SumUt", "Sumatera Barat": "SumBar", "Riau": "RiauProv",
    "Kepulauan Riau": "KepRi", "Jambi": "Jambi", "Sumatera Selatan": "SumSel",
    "Bangka-Belitung": "BaBel", "Bengkulu": "Bengkulu", "Lampung": "Lampung",
    "Jakarta Raya": "DKI", "Jawa Barat": "JaBar", "Banten": "Banten", "Jawa Tengah": "JaTeng",
    "Yogyakarta": "DIY", "Jawa Timur": "JaTim", "Bali": "Bali",
    "Kalimantan Barat": "KalBar", "Kalimantan Tengah": "KalTeng", "Kalimantan Selatan": "KalSel",
    "Kalimantan Timur": "KalTim", "Kalimantan Utara": "KalUt",
    "Sulawesi Utara": "SulUt", "Gorontalo": "Gorontalo", "Sulawesi Tengah": "SulTeng",
    "Sulawesi Selatan": "SulaSel", "Sulawesi Barat": "SulBar", "Sulawesi Tenggara": "SulTra",
    "Nusa Tenggara Barat": "NTB", "Nusa Tenggara Timur": "NTT",
    "Maluku": "Maluku", "Maluku Utara": "MalUt", "Papua Barat": "PapuaBar", "Papua": "PapuaProv",
}

gdf = gpd.read_file('mapdata/indonesia.geojson')
gdf['abbr'] = gdf['state'].map(name_to_abbr)
assert gdf['abbr'].isna().sum() == 0, gdf[gdf['abbr'].isna()]

gdf['genCPI_S1'] = gdf['abbr'].map(lambda a: table4[a][0])
gdf['genCPI_S2'] = gdf['abbr'].map(lambda a: table4[a][1])
gdf['genCPI_S3'] = gdf['abbr'].map(lambda a: table4[a][2])
gdf['realGDP_S1'] = gdf['abbr'].map(lambda a: table4[a][6])
gdf['realGDP_S2'] = gdf['abbr'].map(lambda a: table4[a][7])
gdf['realGDP_S3'] = gdf['abbr'].map(lambda a: table4[a][8])
gdf['adjHHC_S1'] = gdf['abbr'].map(lambda a: table4[a][9])
gdf['adjHHC_S2'] = gdf['abbr'].map(lambda a: table4[a][10])
gdf['adjHHC_S3'] = gdf['abbr'].map(lambda a: table4[a][11])
gdf['foodCPI_S1'] = gdf['abbr'].map(lambda a: foodCPI[a][0])
gdf['foodCPI_S2'] = gdf['abbr'].map(lambda a: foodCPI[a][1])
gdf['foodCPI_S3'] = gdf['abbr'].map(lambda a: foodCPI[a][2])

# each map gets its OWN independent color scale (no sharing across scenarios or indicators)
indicators = ['genCPI', 'foodCPI', 'realGDP', 'adjHHC']
titles = {'genCPI': 'General CPI (%)', 'foodCPI': 'Food CPI (%)',
          'realGDP': 'Real GDP (%)', 'adjHHC': 'Adjusted HHC (%)'}
scenario_names = {'S1': 'Protection', 'S2': 'Free Trade', 'S3': 'Productivity'}

# On-brand diverging colormaps built from the deck's own Lehigh-theme colors:
# bad end = luredk20 (#c53c33), neutral = lubrown10 (#e4dad1), good end = lugreenk60 (#3d6762)
_bad_to_good = LinearSegmentedColormap.from_list(
    'brand_bad_good', ['#c53c33', '#e4dad1', '#3d6762'])
_good_to_bad = LinearSegmentedColormap.from_list(
    'brand_good_bad', ['#3d6762', '#e4dad1', '#c53c33'])
# CPI: higher = worse (inflation) -> red end = high/bad, green end = low/good
# Real GDP / Adjusted HHC: higher = better -> green end = high/good, red end = low/bad
cmaps = {'genCPI': _good_to_bad, 'foodCPI': _good_to_bad, 'realGDP': _bad_to_good, 'adjHHC': _bad_to_good}

mpl.rcParams['font.family'] = 'DejaVu Serif'

for s in ['S1', 'S2', 'S3']:
    for ind in indicators:
        vals = gdf[f'{ind}_{s}']
        vmin, vmax = vals.min(), vals.max()
        fig, ax = plt.subplots(figsize=(5.0, 3.15))
        norm = TwoSlopeNorm(vmin=vmin, vcenter=0 if vmin < 0 < vmax else (vmin + vmax) / 2, vmax=vmax)
        gdf.plot(column=f'{ind}_{s}', ax=ax, cmap=cmaps[ind], norm=norm,
                  edgecolor='white', linewidth=0.3, legend=True,
                  legend_kwds={'orientation': 'horizontal', 'location': 'bottom',
                               'shrink': 0.45, 'aspect': 28, 'pad': 0.03})
        cax = fig.axes[-1]
        cax.tick_params(labelsize=7, length=2, color='#88644b', labelcolor='#6b4226')
        for spine in cax.spines.values():
            spine.set_visible(False)
        ax.set_title(titles[ind], fontsize=13, color='#502d0e')
        ax.axis('off')
        ax.set_xlim(94, 142)
        ax.set_ylim(-12, 7)
        fig.tight_layout()
        outpath = f'map_{s}_{ind}.png'
        fig.savefig(outpath, dpi=200, transparent=True)
        plt.close(fig)
        print('saved', outpath, f'range=({vmin:.2f},{vmax:.2f})')
