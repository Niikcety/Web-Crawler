from .controller import ApplicationController

class ApplicationView():
    def __init__(self):
        self.controller = ApplicationController()

    def start(self):
        print('''Hello! This is WebCrawler v.1
                Here are the options:
                1. start_crawling(Type "start")
                2. show_statistics (Type "statistics")
                3. help (type "help")
                4. exit (Type "exit")
            ''')
        while True:
            user_input = input('Please type your input')
            if user_input == 'start':
                self.crawl()
            elif user_input == 'statistics':
                pass
            elif user_input == 'help':
                pass
            elif user_input == 'exit':
                return
            else:
                print('Invalid input! Please try again!')

    def crawl(self):
        self.controller.crawl()

    def statistics(self):
        pass

    def help(self):
        pass
