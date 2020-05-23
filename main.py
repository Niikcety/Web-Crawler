from Application.controller import ApplicationController
from Statistics.statistics_utils import get_by_server_type_time

def main():
    application = ApplicationController()
    application.start()


if __name__ == '__main__':
    # main()
    # print(get_by_server_type_time(day=1))
