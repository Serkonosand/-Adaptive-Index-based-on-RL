import random


FILEPATH = "./testdata/data.txt"
if __name__ == '__main__':
    with open(FILEPATH, 'w') as f:
        for i in range(10):
            for j in range(100):
                if i % 2 == 0:
                    f.write(str(0)+'\n')
                else:
                    f.write(str(1)+'\n')
