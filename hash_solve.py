import hashlib, logging, time, pickle

# Class LoggingControl which activates logging.
# Defines methods for each of the custom messages that will appear in the log
class LoggingControl:
    def __init__(self):
        logging.basicConfig(
            filename='results.log',                                       # States the file to be used
            level=logging.DEBUG,
            format='[%(asctime)s] %(levelname)s: %(message)s',            # Defines the format of the log message
            datefmt= '%m/%d/%Y %I:%M:%S %p'
        )

    # Method that logs an INFO message stating that the hash process has begun.
    def initiation(self):
        logging.info("Starting to process 'hash'.")

    # Method that logs a DEBUG message stating which passcode is being hashed
    # and with was algorithm it is using to hash it.
    def valueTried(self, pc, algo):
        logging.debug("Trying value %s with %s.", pc, algo)

    # Method that logs an INFO message stating that a potential solution has been found.
    def possibleSolution(self, solution):
        logging.info("Possible solution identified as: %s.", solution)


# Dictionary of hash algorithms to be used for hashing the passcodes.
alg = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

# Creates an object called logger from the class LoggingControl()
# This will allow for the class methods to be called in order to log actions in results.log
logger = LoggingControl()

# Creates a new log in file results.log.
# Writes to the file the given string.
with open("results.log", "w") as l:
    l.write("This is a new log file.\n")

# Read the hash in pickled file password.dat
# initiation() called to log that the hashing process has begun.
with open("password.dat", 'rb') as p:
    logger.initiation()
    data = pickle.load(p)

    print(f'The password hash is: {data}')

## Creating all 4 digit (0-9) combinations

# List of all possible numbers used for the passcode,
# listing them as str values to aid with the making of combinations.
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Create a list to store all the created passcodes.
comboList = []
# Use nested for loops to iterate through the values in numList,
# and concatenating them into "passcodes".
for n1 in numList:
    for n2 in numList:
        for n3 in numList:
            for n4 in numList:
                p = n1 + n2 + n3 + n4

                comboList.append(p)

## Create hash for each 4 digit combo with each algorithm in dictionary

# Nested for loop system that:
# 1) Iterates through each passcode.
# 2) Iterates through each algorithm.
# 3) Hashes the given passcode with each algorithm.
# 4) Stores the hashed passcodes into the list createdHashes.
# 5) valueTried() is called to state the passcode tried and the algorithm it is being hashed with.
# 6) Iterates through each passcode hash.
# 7) Compares the provided hash with each passcode hash till a match is found.
# 8) If no match found, steps 1 - 7 repeated.
#    Otherwise, possibleSolution() is called to state a possible match was found.

# Create a list to store all the created passcode hashes.
createdHashes = []
# 1)
for passcode in comboList:
    # 2)
    for a in alg:
        h = hashlib.new(a, passcode.encode('utf-8')).hexdigest()            # 3)
        createdHashes.append(h)                                             # 4)

        logger.valueTried(passcode, a)                                      # 5)

    # 6)
    for c in createdHashes:
        if data == c:                                                       # 7)
            logger.possibleSolution(passcode)                               # 8)
            print(f'Using hash {a}, the possible password is: {passcode}')

            quit()                                                          # If a match is found, the program is ended.