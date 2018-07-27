from proxypool.api import app
from proxypool.schedule import Schedule
import platform

def main():
    s = Schedule()
    s.run()
    operation = platform.platform()
    if 'Linux' in operation:
        app.run(host="0.0.0.0",port='5000')
    else:
        app.run()

if __name__ == '__main__':
    main()
