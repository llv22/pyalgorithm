# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.7
# ---

# # Solution for Global Minimial

from time import time

# $$ f(x)=x^3-60x^2-4x+6 $$, 求x在[0,100]范围内f(x)最小值

# $$f'(x) = 3x^2 - 120x - 4$$
#
# $$ x_{n+1} = x_{n} - \frac{f(x_n)}{f'(x_n)} $$

# # Newton for f'

start = time()

x0 = 100
x1 = x0 - (3*(x0**2) - 120 * x0 - 4) / (6 * x0 - 120)
f_val = (x0 ** 3) - 60 * (x0**2) - 4 * x0 + 6

while f_val > 1e-8:
    x1 = x0 - (3*(x0**2) - 120 * x0 - 4) / (6 * x0 - 120)
    x0 = x1
    f_val = 3*(x0**2) - 120 * x0 - 4

print("Newton method for f' is about : %0.2f seconds" % (time() - start))

x0

(x0 ** 3) - 60 * (x0**2) - 4 * x0 + 6

# # Gradient Descent
#
# $$ f(x)=x^3-60x^2-4x+6 $$

import tensorflow as tf
from tensorflow.train import AdamOptimizer

start = time()

x = tf.get_variable('x', initializer=tf.constant(100.0))
y = x * x * x - 60 * x * x - 4 * x + 6

# +
optimizer = AdamOptimizer(learning_rate=1e-2).minimize(y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(50000):
        sess.run(optimizer)
    print(sess.run(x))
# -

print("Gradient Descent for y is about : %0.2f seconds" % (time() - start))

# # Binary Search
#
# similiar to Newton method from [0, 100]. Somehow simple, just skip it

# # MCTS

import random

start = time()

min_val = (lambda x: x**3 + 6)(100)
solution = 100
best_step = 0
delta_value = 100000; delta_no_improve = 0
fv_pre = (lambda v: v**3 - 60 * (v**2) - 4 * v + 6)(solution)
i = 0
# for i in range(1000000):
#     1. only integer number
#     v = random.randrange(0, 100.0)
#     2. sample uniform between [0, 1) * 100.0
while delta_no_improve < 200000:
    v = random.random() * 100
    fv = (lambda v: v**3 - 60 * (v**2) - 4 * v + 6)(v)
    if min_val > fv:
        min_val = fv
        solution = v
        best_step = i
        delta_value = 100000; delta_no_improve = 0
    else:
        if abs(fv_pre - fv) < delta_value:
            delta_value = abs(fv_pre - fv)
        else:
            delta_no_improve += 1
    fv_pre = fv; i += 1

print("Random MCTS is about : %0.2f seconds" % (time() - start))

delta_value

delta_no_improve

min_val

best_step

solution

# # MCTS - Exploration with f' as penality
#
# Sample with **Uniform Distribution** to select better seed

import random
import numpy as np

start = time()

# +
min_val = (lambda x: x**3 + 6)(100)
solution = 100
best_penality = 1000000
best_step = 0
no_improve = 0
seed = 0
minv_region = 1; maxv_region = -1; sample_region_n = 0
delta_value = 100000; delta_no_improve = 0
fv_pre = (lambda v: v**3 - 60 * (v**2) - 4 * v + 6)(solution)
i = 0

while delta_no_improve < 200000:
# for i in range(1000000):
    if no_improve < 10000 or sample_region_n < 100:
        seed = random.random()
    else:
        # uniform seems still not very good, how about gaussion?
        seed = np.random.uniform(minv_region, maxv_region)
    v = seed * 100
    fv = (lambda v: v**3 - 60*(v**2) - 4 * v + 6)(v)
    penality = (lambda x: x**3 - 60*(x**2) - 4*x + 6)(v)
    if abs(penality) < best_penality:
        best_penality = abs(penality)
        no_improve = 0
        minv_region = 1; maxv_region = -1; sample_region_n = 0
    else:
        no_improve += 1
        if no_improve > 10000:
            if v > maxv_region:
                maxv_region = seed
            if v < minv_region:
                minv_region = seed
            sample_region_n += 1
        
    if min_val > fv:
        min_val = fv
        solution = v
        best_step = i
    else:
        if abs(fv_pre - fv) < delta_value:
            delta_value = abs(fv_pre - fv)
        else:
            delta_no_improve += 1
    fv_pre = fv; i += 1
# -

print("MCTS with uniform sampling for exploration is about : %0.2f seconds" % (time() - start))

delta_value

delta_no_improve

min_val

solution

best_step

# # MCTS - Exploration with f' as penality
#
# Sample with **Gaussion Distribution** to select better seed
#
# Too costy for calcuation of $\delta$ for Gaussian distribution, set $\delta$ = 0.01

import random
import numpy as np

start = time()

# +
min_val = (lambda x: x**3 + 6)(100)
solution = 100
best_penality = 1000000
best_step = 0
no_improve = 0
seed = 0
minv_region = 1; maxv_region = -1; sample_region_n = 0; sample_mean = 0
delta_value = 100000; delta_no_improve = 0
fv_pre = (lambda v: v**3 - 60 * (v**2) - 4 * v + 6)(solution)
i = 0

while delta_no_improve < 200000:
# for i in range(1000000):
    if no_improve < 10000 or sample_region_n < 1000:
        seed = random.random()
    else:
        # uniform seems still not very good, how about gaussion?
        seed = np.random.normal(sample_mean, 0.01, 1)[0]
    v = seed * 100
    fv = (lambda v: v**3 - 60*(v**2) - 4 * v + 6)(v)
    penality = (lambda x: x**3 - 60*(x**2) - 4*x + 6)(v)
    if abs(penality) < best_penality:
        best_penality = abs(penality)
        no_improve = 0
        minv_region = 1; maxv_region = -1; sample_region_n = 0
    else:
        no_improve += 1
        if no_improve > 10000:
            if v > maxv_region:
                maxv_region = seed
            if v < minv_region:
                minv_region = seed
            sample_mean = (sample_region_n * sample_mean + seed) / (sample_region_n + 1)
            sample_region_n += 1
        
    if min_val > fv:
        min_val = fv
        solution = v
        best_step = i
    else:
        if abs(fv_pre - fv) < delta_value:
            delta_value = abs(fv_pre - fv)
        else:
            delta_no_improve += 1
    fv_pre = fv; i += 1
# -

print("MCTS with gaussion sampling for exploration is about : %0.2f seconds" % (time() - start))

delta_value

delta_no_improve

min_val

solution

best_step


