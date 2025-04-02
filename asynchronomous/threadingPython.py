import threading;
from concurrent.futures import ThreadPoolExecutor;
import time;
import requests;

def funcitons(secs):
    print('the function is sleeping for the next {} secs'.format(secs));
    time.sleep(secs);
    print('the function sleeped for {}'.format(secs));

def main():
#counting the time with performance counter 
    time1 = time.perf_counter();
    e1 = threading.Thread(target=funcitons, args=[5]);
    e2 = threading.Thread(target=funcitons, args=[2]);
    e3 = threading.Thread(target=funcitons, args=[51]);

    e1.start()
    e2.start()
    e3.start()

    e1.join();
    e2.join();
    e3.join();

    time2 = time.perf_counter();
    print(time2-time1);

def pool():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(funcitons, 3);
        future2 = executor.submit(funcitons, 5);
        future3 = executor.submit(funcitons, 2);

        #returns none
        print(future1.result());
        print(future2.result());
        print(future3.result());

# pool();
def fileDownloader(url, name):
    print(f'started downloading :{name} file');
    r = requests.get(url)
    open(f'files3/file{name}.jpg', 'wb').write(r.content);
    print(f'finished downloading :{name} file');
    

#with submit and results
def demoPool():
    url = 'https://picsum.photos/2000/3000'
    for i in range(5):
        with ThreadPoolExecutor() as e:
            future = e.submit(fileDownloader, url, i);

    print(future.result());
# demoPool();


def mapDemoPool():
    l = [5, 4, 2, 3, 5];
    with ThreadPoolExecutor() as e:
        futures = e.map(funcitons, l);#it does not returns and it only prints and execute thr function 
        for future in futures:
            print(future);#it returns the execute value if nothing shows none

mapDemoPool();