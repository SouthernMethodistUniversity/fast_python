def gauss_legendre_pi(d):
    a = 1.
    b = 2.**(-1/2)
    t = 1./4
    p = 1.
    threshold_not_met = True
    while threshold_not_met:
        if a-b > d:
            an = (a+b)/2
            bn = (a*b)**(1/2)
            tn = t-p*(a-an)**2
            pn = 2*p
            pi = ((an+bn)**2)/(4*tn)
            a = an
            b = bn
            t = tn
            p = pn
        else:
            threshold_not_met = False
    return pi
