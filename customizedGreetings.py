import sys

def customized_hello( gender_prefix, first_name, last_name):
    print("Hello %s %s %s!" % ( gender_prefix, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)
    gender_prefix = sys.argv[1]
    first_name = sys.argv[2]
    last_name = sys.argv[3]
    customized_hello( gender_prefix,first_name, last_name)