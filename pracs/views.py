from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import imageio
import urllib, base64
import random
import math



def index(request):
    return render(request, 'HomePage.html')


def p(request):
    return render(request, 'practicals.html')


def p1(request):
    return render(request, 'p1.html')


def L1(request):
    t1 = float(request.GET["t1"])
    t2 = float(request.GET["t2"])
    t3 = float(request.GET["t3"])
    t4 = float(request.GET["t4"])
    t5 = float(request.GET["t5"])
    n1 = float(request.GET["n1"])
    n2 = float(request.GET["n2"])
    n3 = float(request.GET["n3"])
    n4 = float(request.GET["n4"])
    n5 = float(request.GET["n5"])
    r1 = float(request.GET["r1"])
    r2 = float(request.GET["r2"])
    r3 = float(request.GET["r3"])
    r4 = float(request.GET["r4"])
    r5 = float(request.GET["r5"])
    c1 = round(math.cos(math.radians(t1)), 4)
    c2 = round(math.cos(math.radians(t2)), 4)
    c3 = round(math.cos(math.radians(t3)), 4)
    c4 = round(math.cos(math.radians(t4)), 4)
    c5 = round(math.cos(math.radians(t5)), 4)
    x1 = round((n1 / r1), 3)
    x2 = round((n2 / r2), 3)
    x3 = round((n3 / r3), 3)
    x4 = round((n4 / r4), 3)
    x5 = round((n5 / r5), 3)

    x = [c1, c2, c3, c4, c5]
    y = [x1, x2, x3, x4, x5]
    xax = np.array(x)
    yax = np.array(y)
    plt.plot(xax, yax, 'o')
    b, a = np.polyfit(xax, yax, 1)
    plt.plot(xax, b * xax + a, color="k", lw=2.5)
    plt.ylabel('Tsquare - axis')
    plt.xlabel('y(cm) - axis')
    plt.title('A graph of cos(Θ) vs x')
    b = round((b),3)
    a = round((a),3)
    plt.show()
    plt.savefig("desktop/graph.jpg")

    return render(request, 's1.html', {
                                             "t1": t1,
                                             "t2": t2,
                                             "t3": t3,
                                             "t4": t4,
                                             "t5": t5,
                                             "c1": c1,
                                             "c2": c2,
                                             "c3": c3,
                                             "c4": c4,
                                             "c5": c5,
                                             "n1": n1,
                                             "n2": n2,
                                             "n3": n3,
                                             "n4": n4,
                                             "n5": n5,
                                             "r1": r1,
                                             "r2": r2,
                                             "r3": r3,
                                             "r4": r4,
                                             "r5": r5,
                                             "x1": x1,
                                             "x2": x2,
                                             "x3": x3,
                                             "x4": x4,
                                             "x5": x5,
                                             "b": b,
                                             "a": a,

                                             })



def p2(request):
    return render(request, 'p2.html')


def p3(request):
    return render(request, 'p3.html')


def L3(request):
    u1 = float(request.GET["u1"])
    u2 = float(request.GET["u2"])
    u3 = float(request.GET["u3"])
    u4 = float(request.GET["u4"])
    u5 = float(request.GET["u5"])
    v1 = float(request.GET["v1"])
    v2 = float(request.GET["v2"])
    v3 = float(request.GET["v3"])
    v4 = float(request.GET["v4"])
    v5 = float(request.GET["v5"])
    c1 = round((1 / u1), 4)
    c2 = round((1 / u2), 4)
    c3 = round((1 / u3), 4)
    c4 = round((1 / u4), 4)
    c5 = round((1 / u5), 4)
    d1 = round((1 / v1), 4)
    d2 = round((1 / v2), 4)
    d3 = round((1 / v3), 4)
    d4 = round((1 / v4), 4)
    d5 = round((1 / v5), 4)
    f1 = round(((u1 + v1)/(u1*v1)), 4)
    f2 = round(((u2 + v2)/(u2*v2)), 4)
    f3 = round(((u3 + v3)/(u3*v3)), 4)
    f4 = round(((u4 + v4)/(u4*v4)), 4)
    f5 = round(((u5 + v5)/(u5*v5)), 4)

    x = [c1, c2, c3, c4, c5]
    y = [d1, d2, d3, d4, d5]
    xax = np.array(x)
    yax = np.array(y)
    plt.plot(xax, yax, 'o')
    b, a = np.polyfit(xax, yax, 1)
    plt.plot(xax, b * xax + a, color="k", lw=2.5)
    plt.ylabel('Tsquare - axis')
    plt.xlabel('y(cm) - axis')
    plt.title('A graph of cos(Θ) vs x')
    b = round((b),3)
    a = round((a),3)
    v = plt.show()

    return render(request, 's3.html', {
                                             "u1": u1,
                                             "u2": u2,
                                             "u3": u3,
                                             "u4": u4,
                                             "u5": u5,
                                             "c1": c1,
                                             "c2": c2,
                                             "c3": c3,
                                             "c4": c4,
                                             "c5": c5,
                                             "v1": v1,
                                             "v2": v2,
                                             "v3": v3,
                                             "v4": v4,
                                             "v5": v5,
                                             "d1": d1,
                                             "d2": d2,
                                             "d3": d3,
                                             "d4": d4,
                                             "d5": d5,
                                             "f1": f1,
                                             "f2": f2,
                                             "f3": f3,
                                             "f4": f4,
                                             "f5": f5,
                                             "v": v,
                                             "b": b,
                                             "a": a,
    })
def p4(request):
    return render(request, 'p4.html')


def L4(request):
    l = float(request.GET["l"])
    t1 = float(request.GET["y1"])
    t2 = float(request.GET["y2"])
    t3 = float(request.GET["y3"])
    t4 = float(request.GET["y4"])
    t5 = float(request.GET["y5"])
    n1 = float(request.GET["11"])
    n2 = float(request.GET["12"])
    n3 = float(request.GET["13"])
    n4 = float(request.GET["14"])
    n5 = float(request.GET["15"])
    r1 = float(request.GET["21"])
    r2 = float(request.GET["22"])
    r3 = float(request.GET["23"])
    r4 = float(request.GET["24"])
    r5 = float(request.GET["25"])
    c1 = t1 - n1
    c2 = t2 - n2
    c3 = t3 - n3
    c4 = t4 - n4
    c5 = t5 - n5
    x1 = (r1**2) - (c1**2)
    x2 = (r2**2) - (c2**2)
    x3 = (r3**2) - (c3**2)
    x4 = (r4**2) - (c4**2)
    x5 = (r5**2) - (c5**2)
    x = [c1, c2, c3, c4, c5]
    y = [x1, x2, x3, x4, x5]
    xax = np.array(x)
    yax = np.array(y)
    plt.plot(xax, yax, 'o')
    b, a = np.polyfit(xax, yax, 1)
    plt.plot(xax, b * xax + a, color="k", lw=2.5)
    plt.ylabel('Tsquare - axis')
    plt.xlabel('y(cm) - axis')
    plt.title('A graph of cos(Θ) vs x')
    b = round((b), 3)
    a = round((a), 3)
    v = plt.show()

    return render(request, 's4.html', {
                                            "t1": t1,
                                            "t2": t2,
                                            "t3": t3,
                                            "t4": t4,
                                            "t5": t5,
                                            "c1": n1,
                                            "c2": n2,
                                            "c3": n3,
                                            "c4": n4,
                                            "c5": n5,
                                            "n1": r1,
                                            "n2": r2,
                                            "n3": r3,
                                            "n4": r4,
                                            "n5": r5,
                                            "r1": c1,
                                            "r2": c2,
                                            "r3": c3,
                                            "r4": c4,
                                            "r5": c5,
                                            "x1": x1,
                                            "x2": x2,
                                            "x3": x3,
                                            "x4": x4,
                                            "x5": x5,
                                            "v": v,
                                            "b": b,
                                            "a": a,
                                        })


def p5(request):
    return render(request, 'p5.html')


def p6(request):
    return render(request, 'p6.html')


def p7(request):
    return render(request, 'p7.html')


def p8(request):
    return render(request, 'p8.html')


def p9(request):
    return render(request, 'p9.html')