#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import choice


def list_choice(in_list,p_list=[]):
    # 生成数列
    length=len(in_list)
    l=list(np.arange(0,length))
    if not p_list:
        _str =in_list[choice(l)]
    else:
         _str =in_list[choice(l,p=p_list)]
    return  _str
