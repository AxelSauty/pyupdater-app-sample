from pyupdater.client import Client
from client_config import ClientConfig


class Main:

    client = None

    APP_NAME = 'test-app'
    APP_VERSION = '0.0.1'

    def start(self):
        print(self.APP_VERSION)
        self.init_client()
        self.check_for_update()

    # create a pyupdater client and set progress hook
    def init_client(self):
        self.client = Client(ClientConfig())
        self.client.refresh()
        self.client.add_progress_hook(self.print_status_info)

    # check if the distant server has an update available, download and install if possible
    def check_for_update(self):
        print('Checking for update')
        app_update = self.client.update_check(self.APP_NAME, self.APP_VERSION)
        if app_update is not None:
            print('Update found, downloading...')
            app_update.download()
            # if app_update.is_downloaded():
            #     print('Upload downloaded, extracting...')
            #     app_update.extract_overwrite()
            if app_update.is_downloaded():
                print('Upload downloaded, restarting...')
                app_update.extract_restart()
        print('No update found')

    # print download progress of the update
    def print_status_info(self, info):
        total = info.get(u'total')
        downloaded = info.get(u'downloaded')
        status = info.get(u'status')
        print(downloaded, total, status)


if __name__ == '__main__':
    main = Main()
    main.start()