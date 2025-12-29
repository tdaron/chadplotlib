import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import importlib

def makeMeAChad():
    # font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Bold.ttf")
    font_manager.fontManager.addfont(path=path)
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Medium.ttf")
    font_manager.fontManager.addfont(path=path)
    path = importlib.resources.files(__name__).joinpath("fonts/Montserrat-Regular.ttf")
    font_manager.fontManager.addfont(path=path)
    mpl.rcParams['font.family'] = 'Montserrat'
    mpl.rcParams['font.weight'] = 600
    plt.rcParams['axes.titleweight'] = 600
    plt.rcParams['axes.labelweight'] = 600

    # plt.rcParams['axes.facecolor'] = '#f0f0f0'
    plt.rcParams.update({'font.size': 13})
    print('chad setup ok')

def showExample():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    product_a_sales = [150, 180, 210, 190, 170, 220, 240, 200, 210, 230, 190, 250]
    product_b_sales = [200, 210, 230, 250, 240, 230, 220, 210, 200, 190, 210, 220]
    product_c_sales = [180, 170, 160, 190, 220, 210, 230, 240, 250, 220, 200, 190]
    plt.plot(months, product_a_sales, label='Product A', marker='o')
    plt.plot(months, product_b_sales, label='Product B', marker='o')
    plt.plot(months, product_c_sales, label='Product C', marker='o')
    plt.xlabel('Months')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data for Products A, B, and C')
    plt.legend()
    plt.grid(True)
    plt.show()
