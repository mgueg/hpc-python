 vi setup.py 
 python3 setup.py build_ext --inplace
 python3 -m cProfile -o profile.dat mandel_main.py 
 python3 -m pstats profile.dat
    strip
    sort time
    stats 10
