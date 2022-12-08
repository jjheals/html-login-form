
from pickle import dump, load
from os import getcwd, chdir
from User import User

workingDir = r"c:\Users\Justin\OneDrive\Coding Practice and Apps\web-stuff\vuln-website\backend"
if getcwd() != workingDir: chdir(workingDir)

from hashlib import sha256

def authenticate(inputUsername, inputPass):
    print(f'authenticating {inputUsername} ...')
    with open('users.dat', 'rb') as file: 
        l = load(file)

    eInputPass = User.encrypt(inputPass)
    a = False # Tracks if user was authenticated or not

    for user in l:
        if user.username == inputUsername:
            if user.password == eInputPass:
                a = True
                break
    
    return a

def saveUser(username, password):
    newUser = User(username, password)

    print(f'creating user : {username}')

    # Load a list of all the users, add this new user to the list 
    with open('users.dat', 'rb') as rfile:
        try:
            users = load(rfile)
        except EOFError: 
            users = []
    
    print(f'users before adding {username}')
    print(users)

    users.append(newUser)

    print(f'users after adding {username}')
    print(users)

    # Sync the database 
    with open('users.dat', 'wb') as wfile:
        dump(users, wfile)

    # Save the username to users.txt
    # NOTE: could encrypt usernames, but if attacker has access to users.dat this is futile
    #       b/c to efficiently* use usernames as login information they need to be plaintext
    #       and usernames are identity not sensitive (but not PII)
    with open('usernames.txt', 'a') as sfile:
        sfile.write(f'{username}\n') 

    return 


# Returns 0 if passwords do not match
# Returns 1 if username already exists
# Returns 2 if user creation was successful 
def createNewUser(username, password, confPass):

    if confPass != password: return 0

    # Check if username already exists
    with open('usernames.txt', 'r') as file:
        usernames = file.read().splitlines()
        for u in file: usernames.append(f'{u}\n')
    print(username)
    print(f'looking for {username} in {usernames}')

    if username in usernames: return 1

    # Create new user
    saveUser(username, password)

    # Return 2 if successful
    return 2




justin = createNewUser('justin', 'password', 'password')
dan = createNewUser('dan', 'danpassword', 'danpassword')
maddie = createNewUser('maddie', 'maddiepassword', 'maddiepassword')
print(f'justin: {justin}')
print(f'dan: {dan}')
print(f'maddie: {maddie}')

print(f'justin auth: {authenticate("justin", "password")}')
print(f'dan auth: {authenticate("dan", "danpassword")}')
print(f'maddie auth: {authenticate("maddie", "maddiepassword")}')
