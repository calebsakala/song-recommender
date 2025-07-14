#!/usr/bin/env python3

string = """def sq_dist(a, b):\n",
    "#     Args: a (ndarray) (n,): vector with n features\n",
    "#     Args: b (ndarray) (n,): vector with n features\n",
    "    n = a.shape[0]\n",
    "    d = 0\n",
    "    for i in range(n):\n",
    "        d+= (a[i] - b[i])**2\n",
    "    return d"""
 
def fix_string(strings):
	strings2 = strings.replace("\n", "")
	strings2 = strings.replace(",", "")
	strings2 = strings.replace('\"', "")
	strings2 = strings.replace('\"', "")
	return strings2

print(fix_string(string))