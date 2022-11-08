from logic.director import Director
# import multiprocessing as mp

if __name__ == '__main__':
    start = Director()
    # processes = [mp.Process(target=start.run, args=()), mp.Process(target=start.run, args=())]
    # processes.append(mp.Process(target=start.run, args=()), mp.Process(target=start.run, args=()))
    # p = mp.Process(target=start.run, args=())
    # p = mp.Process(target=start.run, args=())
    # for p in processes:
        # print('time')
        # p.start()
    # for p in processes:
        # p.join()
    start.run_right()