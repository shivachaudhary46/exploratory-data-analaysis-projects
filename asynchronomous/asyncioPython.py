#asynchronomous in the python 
import asyncio;
import requests;
import time;

# async def fileDOwnloader(url, name):
#     print(f'the file {name} has started downloading :')
#     r = requests.get(url)
#     open(f'files/file{name}.jpg', 'wb').write(r.content);
#     print(f'the file {name} has finished downloading :')
    
# async def main():
#     url = 'https://picsum.photos/3000/2000'
#     for i in range(5):
#         # await fileDOwnloader(url, i);
#         l =await asyncio.gather(fileDOwnloader(url, i));
#         # print(l);

#     # task = asyncio.create_task(fileDOwnloader());
#     # print(task);
#     # l =await asyncio.gather(fileDOwnloader());
#     # print(l);
# asyncio.run(main());

async def function1():
    print('the function 1 is sleeping for the 10 secs');
    time.sleep(10);

async def function2():
    print('the function 2 is sleeping for the 10 secs');
    time.sleep(10);

async def function3():
    print('the function 3 is sleeping for the 10 secs');
    time.sleep(10);

async def main():
    # await function1()
    # await function2()
    # await function3()

    # task = asyncio.create_task(function1());
    # print(task)
    task = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    );
    print(task);

asyncio.run(main());