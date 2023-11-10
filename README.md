# CrackingTheHash
Implementing logging in order to track the process of unpickling a picked hash and finding a potential matching hash of a theoretical passcode. 

## password.dat
    * Contains the picked hash that needs to be "unpickled".

## results.log
    * Logging file that receives the log messages and provides time-stamped entries for the program.
    * Documents the each hashing algorithm used and the current four-digit combination that is being hashed and compared.
    
## hash_solve.py
    * Contains the code for logging the process of finding a matching hash to the picked hash.
    * The passcodes are the four-digit combinations of the values 0-9.
    * The module hashlib gives the various hashing algorithms to hash the four digit combinations and find a matching hash to the unpickled hash.
