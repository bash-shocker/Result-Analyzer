def text():
    import time
    import sys

    s = '.'
    #sys.stdout.write( '\n\n\tDownloading attendance sheet' )
    i=1
    while i<52:
        sys.stdout.write( s )
        sys.stdout.flush()
        time.sleep(0.05)
        i=i+1
    print('\n\n\n\tWELCOME TO KTU ANALYZER\n\n')