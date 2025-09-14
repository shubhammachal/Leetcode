import threading
class H2O:
    def __init__(self):

        self.semaphore_h = threading.Semaphore(2)
        self.semaphore_o = threading.Semaphore(1)

        self.barrier = threading.Barrier(3)



    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.semaphore_h:
            self.barrier.wait()
            releaseHydrogen()
        


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.semaphore_o:
            self.barrier.wait()
            releaseOxygen()
        