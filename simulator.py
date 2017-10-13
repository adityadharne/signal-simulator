from models import Signal
import sys
import time


def console():
    """
    Console display driver and user interaction point 
    """
    while True:
        try:
            print "CHOOSE BETWEEN THE OPTIONS AND ENTER THE CORRESPONDING NUMBER:"
            print "1. ONE-TIME SIMULATION"
            print "2. AUTO SIMULATE"
            print "3. EXIT THE SIMULATOR"
            user_choice = int(raw_input("ENTER YOUR CHOICE: "))
            if user_choice == 1:
                lanes = multi_lane()
                run_simulator(user_choice, lanes)
            elif user_choice == 2:
                lanes = multi_lane()
                run_simulator(user_choice, lanes)
            elif user_choice == 3:
                print "EXITING TRAFFIC LIGHT SIMULATOR"
                sys.exit()
            else:
                print "ENTER VALID CHOICE"
        except (KeyboardInterrupt, EOFError, ValueError):
            print "\nINVALID INPUT. PLEASE TRY AGAIN"


def multi_lane():
    number_lanes = int(raw_input("ENTER NUMBER OF LANES. MAX = 4: "))
    if number_lanes > 4 or number_lanes < 1:
        print "OUT OF BOUNDS!"
        multi_lane()
    else:
        return number_lanes


def run_simulator(user_choice, lanes):
    """
    Runs the simulator 
    :param user_choice: User input choice
    """
    direction = (raw_input("IS THIS SIGNAL FOR A TURNING? ENTER 'y' FOR 'YES' OR ANY OTHER KEY FOR 'NO': "))
    if direction == 'y':
        direction = int(raw_input("ENTER 1 FOR RIGHT TURN OR 0 FOR LEFT TURN: "))

    print "ENTER DURATION FOR EACH SIGNAL COLOR IN SECONDS"
    green = clean_duration("DURATION FOR GREEN LIGHT: ")
    red = clean_duration("DURATION FOR RED LIGHT: ")
    yellow = clean_duration("DURATION FOR YELLOW LIGHT: ")

    simulated_signal = Signal(green_duration=green, yellow_duration=yellow, red_duration=red, direction=direction)
    iterations = 1
    try:
        if user_choice == 1:
            simulate(simulated_signal, iterations, lanes)
        if user_choice == 2:
            print "\nNOTE: ENTER 'CONTROL + C' TO ABORT\n"
            number_iterations = int(raw_input("ENTER NUMBER OF ITERATIONS: "))
            simulate(simulated_signal, iterations * number_iterations, lanes)
    except (KeyboardInterrupt, EOFError):
        print ""


def clean_duration(user_prompt):
    """
    Cleans signal duration input
    :param user_prompt: Console output prompt for each signal
    :return: Cleaned signal duration
    """
    cleaned_duration = float(raw_input(user_prompt))
    while True:
        try:
            if cleaned_duration > 0:
                return cleaned_duration
            else:
                raise ValueError()
        except ValueError:
            print "DURATION MUST BE POSITIVE. PLEASE TRY AGAIN"
            cleaned_duration = float(raw_input(user_prompt))


def iterate(simulated_signal, lanes):
    """
    Transitions each ASCII signal through iterations and displays on console
    :param simulated_signal: Signal
    """
    signal_duration_left = simulated_signal.signals_duration[simulated_signal.signal_now]
    signal_duration_elapsed = 0
    while signal_duration_elapsed < signal_duration_left:
        # print ("                  \n"
        #        " TRANSITIONS TO   \n"
        #        "      ||          \n"
        #        "      \/          \n")
        print simulated_signal.ascii_signals[simulated_signal.signal_now] * lanes
        # print "\n"
        if signal_duration_left - signal_duration_elapsed >= 1:
            time.sleep(1)
        elif signal_duration_left - signal_duration_elapsed >= 0:
            time.sleep(signal_duration_elapsed)
        signal_duration_elapsed += 1
    simulated_signal.signal_transition()


def simulate(simulated_signal, iterations, lanes):
    """
    Simulator for the signals on each iteration
    :param simulated_signal: Signal
    :param iterations: Number of iterations requested
    """
    try:
        sim_count = 0
        while sim_count < iterations * 3:
            iterate(simulated_signal, lanes)
            sim_count += 1
    except (KeyboardInterrupt, EOFError, ValueError):
        print "\n"
        print "SIMULATION ABORTED!!!\n"
        print "PRESS 1 TO EXIT OR PRESS ANY OTHER KEY TO START OVER\n"
        abort_input = int(raw_input("YOUR CHOICE: "))
        print "\n"
        if abort_input == 1:
            print "EXITING TRAFFIC LIGHT SIMULATOR"
            sys.exit()
        else:
            console()
