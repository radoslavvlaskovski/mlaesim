
optimum_low = 65
optimum_high = 80

bad_low = 81

good_low = 40
good_high = 64

ok_high = 39

# ALSO NUMBER OF VMS IMPORTANT


def evaluate(cpu_alloc):

    if cpu_alloc <= ok_high :
        return

    if good_low <= cpu_alloc <= good_high:
        return

    if optimum_low <= cpu_alloc <= optimum_high:
        return

    if cpu_alloc >= bad_low:
        return
