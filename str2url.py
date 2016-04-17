def str2url(s):
    #print "liubing haha"
    import urllib2
    #s = '8h2xt132233tFi%5%7_98t%a232%152p2mF%F2714%Fi425F7_.3f.%F4%13mA3n277537p%.eF52E683'
    num_loc = s.find('h')
    #print "num_loc:%d"  % num_loc
    rows = int(s[0:num_loc])
    #print "rows:%d" % rows
    strlen = len(s) - num_loc
    #print "strlen:%d" % strlen
    cols = strlen/rows
    #print "cols:%d" % cols
    right_rows = strlen % rows
    #print "right_rows:%d" % right_rows
    new_s = s[num_loc:]
    output = ''
    for i in xrange(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
            #print "liu1 p x y cols:%d %d %d %d" % (p, x, y, cols)
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
            #print "liu2 p x y cols:%d %d %d %d" % (p, x, y, cols)
        output += new_s[p]
    return urllib2.unquote(output).replace('^','0')
    
