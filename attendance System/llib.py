#!/usr/bin/env python


from multiping import MultiPing
from multiping import multi_ping

if __name__ == "__main__":

    addrs = ["8.8.8.8", "cnn.com", "127.0.0.1", "youtube.com"]

    print("sending one round of pings and checking twice for responses")
    mp = MultiPing(addrs)
    mp.send()
    # First attempt: We probably will only have received response from
    # localhost so far. Note: 0.01 seconds is usually a very unrealistic
    # timeout value. 1 second, or so, may be more useful in a real world
    # example.
    responses, no_responses = mp.receive(0.01)

    print("   received responses:  %s" % list(responses.keys()))
    print("   no responses so far: %s" % no_responses)

    # By now we should have received responses from the others as well
    print("   --- trying another receive ---")
    responses, no_responses = mp.receive(0.1)
    print("   received responses:  %s" % list(responses.keys()))
    print("   still no responses:  %s" % no_responses)
    print("")

    # Sometimes ICMP packets can get lost. It's easy to retry (re-send the
    # ping) to those hosts that haven't responded, yet. Send can be called
    # multiple times and will result in pings to be resent to those addresses
    # from which we have not heard back, yet. Here we try three pings max.
    print("sending again, but waiting with retries if no response received")
    mp = MultiPing(addrs)
    for i in range(3):
        mp.send()
        responses, no_response = mp.receive(0.01)

        print("    received responses:     %s" % list(responses.keys()))
        if not no_response:
            print("    all done, received responses from everyone")
            break
        else:
            print("    %d. retry, resending to: %s" % (i + 1, no_response))
    if no_response:
        print("    no response received in time, even after 3 retries: %s" %
              no_response)
    print("")

    # Fortunately, MultiPing provides a ready-made function to do the retry for
    # you, called send_receive(). Specify the overall timeout and the number of
    # additional retries (which are attempted within this timeout). Omit the
    # 'retry' parameter or set to 0 and there will only be a single send.
    print("sending again, waiting with retries via provided send_receive()")
    responses, no_response = multi_ping(addrs, 0.5, 2)
    print("    reponses: %s" % list(responses.keys()))
    if no_responses:
        print("    no response received in time, even after retries: %s" %
              no_response)