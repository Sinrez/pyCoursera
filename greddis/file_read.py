def main():
    infile = open('philosoph.txt', 'r')

    file_consents = infile.read()

    infile.close()

    print(file_consents)
main()