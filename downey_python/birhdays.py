import random

def has_diplicates(s):

   lst = list(s)
   lst.sort()

   for i in range(len(lst)-1):
       if lst[i] == lst[i+1]:
           return True
       return False

def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.
    n: int
    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.
    num_students: how many students in the group
    num_samples: how many groups to simulate
    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_diplicates(t):
            count += 1
    return count

def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()
