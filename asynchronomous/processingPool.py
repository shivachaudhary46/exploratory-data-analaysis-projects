from concurrent.futures import ProcessPoolExecutor;
#process pool executor is for the long term if users has the many cpu it divides the work for the each cpu processor  and gives the fast result; 
import multiprocessing;
import time;
import requests ;

def functions(secs):
    print(f'the function is sleeping for the {secs} seconds');
    time.sleep(secs);
    print(f'finished {secs} seconds sleeping');

if __name__ == '__main__':
    def processing():

        time1 = time.perf_counter();
        p1 = multiprocessing.Process(target=functions, args=[3]);
        p2 = multiprocessing.Process(target=functions, args=[6]);
        p3 = multiprocessing.Process(target=functions, args=[2]);

        p1.start();
        p2.start();
        p3.start();

        p1.join();
        p2.join();
        p3.join();

        
        time2 = time.perf_counter();
        print(time2-time1);

    # processing();

if __name__ == '__main__':
    def ProcessPool():

        #seconds in the lists
        l = [5, 3, 1, 2, 7];
        time1 = time.perf_counter();
        with ProcessPoolExecutor() as p:
            p1 = p.map(functions, l);
            for iter in p1:
                print(iter);
    # ProcessPool();

#function which download the file 
def fileDownloader(url, name):
    print(f'file has been started downloading {name}');
    response = requests.get(url)
    open(f'files2/file{name}.jpg', 'wb').write(response.content);
    print(f'finished downloading {name}');

#if we use map function in the process it start the downloading simultaneoulsy 
if __name__ == '__main__':
    def processPool():
        url = 'https://picsum.photos/2000/3000';
        l1 = [url for i in range(50)];
        l2 = [i for i in range(50)];
        
        with ProcessPoolExecutor() as pool:
            # p = pool.submit(fileDownloader, url, i);
            # print(p.result());
            p = pool.map(fileDownloader, l1, l2);
            for res in p:
                print(res);

    processPool();