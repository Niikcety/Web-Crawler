from Application.view import ApplicationView
from Statistics.statistics_utils import get_by_server_type_time
import matplotlib.pyplot as plt


def main():
    application = ApplicationView()
    application.start()


if __name__ == '__main__':
    main()
    # print(get_by_server_type_time(day=1))
    # h = get_by_server_type_time(month=1)
    # keys = list(h.keys())
    # values = list(h.values())

    # X = list(range(len(keys)))

    # plt.bar(X, list(h.values()), align="center")
    # plt.xticks(X, keys)

    # plt.title(".bg servers")
    # plt.xlabel("Server")
    # plt.ylabel("Count")
    # plt.show()
    # plt.savefig("Histograms/histogram.png")

    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.show()
    # # SAVE