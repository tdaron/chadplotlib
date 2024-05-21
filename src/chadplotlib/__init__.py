import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import importlib

def makeMeAChad():
    font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Bold.ttf")
    font_manager.fontManager.addfont(path=path)
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Medium.ttf")
    font_manager.fontManager.addfont(path=path)
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Regular.ttf")
    font_manager.fontManager.addfont(path=path)
    mpl.rcParams['font.family'] = 'Montserrat'
    mpl.rcParams['font.weight'] = 800
    # plt.rcParams['axes.facecolor'] = '#f0f0f0'
    plt.rcParams.update({'font.size': 13})
    print('chad setup ok')

