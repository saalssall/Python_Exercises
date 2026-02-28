{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "870361d3-d03a-4aad-b219-b210afbea523",
   "metadata": {},
   "outputs": [],
   "source": [
    "fam =[\"hamid\", 1.86, \"ali\", 1.93, \"zabi\", 1.98, \"rafi\", 1.87]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1f8d9ee3-c1a1-4fe8-93f8-bdabf1246451",
   "metadata": {},
   "outputs": [],
   "source": [
    "fam[7]=1.86 #updating the the seventh element in the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0e93fac3-56f8-4573-bf74-d8314a917403",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hamid', 1.86, 'ali', 1.93, 'zabi', 1.98, 'rafi', 1.86]\n"
     ]
    }
   ],
   "source": [
    "print(fam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3dce6269-9146-4b33-9720-877a016eec64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1.86, 'ali', 1.93, 'zabi', 1.98, 'rafi', 1.86]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6d7f21f3-0cda-480e-8e27-88157f5c3bf4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hamid', 1.86, 'ali', 1.93, 'zabi', 1.98, 'rafi', 1.86]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f858a74a-a5ca-4f80-be13-2d4afe86414a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1.86]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam[-1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "457e42b8-dd8a-4f1e-8067-e0a46577d8e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['ali', 1.93]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam[2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6aeb8c9d-8164-4f33-9b64-9ef67cfe7696",
   "metadata": {},
   "outputs": [],
   "source": [
    "fam[2:4] = [\"haider\", 1.84] #updated the sliced some elements "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c3be7306-86ad-4b8b-b7e2-05c12b6e9ab1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hamid', 1.86, 'haider', 1.84, 'zabi', 1.98, 'rafi', 1.86]\n"
     ]
    }
   ],
   "source": [
    "print(fam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "005c2765-b1d4-4e1d-97b1-15772f394271",
   "metadata": {},
   "outputs": [],
   "source": [
    "fam_full = fam+[\"sima\", 1.76, \"halima\", 1.98] #adding new elements to the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "65464d7d-7833-4d5d-9c6f-be5c1b958a0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hamid',\n",
       " 1.86,\n",
       " 'haider',\n",
       " 1.84,\n",
       " 'zabi',\n",
       " 1.98,\n",
       " 'rafi',\n",
       " 1.86,\n",
       " 'sima',\n",
       " 1.76,\n",
       " 'halima',\n",
       " 1.98]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam_full"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "652ebfad-6f21-4fa1-aec8-eb7156897a1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "del(fam_full[2]) #deleting the element of a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bb1f9899-0d66-4725-b97d-8e739bb27aac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hamid', 1.86, 1.84, 'zabi', 1.98, 'rafi', 1.86, 'sima', 1.76, 'halima', 1.98]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fam_full"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c5b9b1a3-820b-4629-a6d6-3cede13b2132",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4, 'a', 'd']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y= [1,3,4,\"a\",\"d\"] #copying references to the list\n",
    "x=y\n",
    "\n",
    "list(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "23166754-39f9-4b47-873b-aad3cc0c4294",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4, 'a', 'd']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1b2a8e85-ed1e-40a7-a4a3-9de54d819acf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(fam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "838482fc-db87-4d35-8c1f-f4c7b054c2fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(fam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5ded4009-39b9-446b-8553-320d49994c7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function pow in module builtins:\n",
      "\n",
      "pow(base, exp, mod=None)\n",
      "    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments\n",
      "    \n",
      "    Some types, such as ints, are able to use a more efficient algorithm when\n",
      "    invoked using the three argument form.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(pow) #helps you understand the the function of a function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "997d40ee-414a-4b67-aeca-f33c6b89de51",
   "metadata": {},
   "outputs": [],
   "source": [
    "first = [11.25, 18.0, 20.0]\n",
    "second = [10.75, 9.50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3cb07837-64f6-496f-b172-8e5de8ecdfb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11.25, 18.0, 20.0, 10.75, 9.5]\n"
     ]
    }
   ],
   "source": [
    "full = list(first+second) #combined the first and second lists\n",
    "print(full)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "aa2d2757-5356-4584-a1e9-b2a72ab1f921",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20.0, 18.0, 11.25, 10.75, 9.5]\n"
     ]
    }
   ],
   "source": [
    "full_sorted = sorted(full, reverse=True) #sorted the list (full) into descending order\n",
    "print(full_sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3bb48c66-d6f2-48e0-b658-6aad09fdecc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "place = \"poolhouse\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1cb9beb9-5bbf-4bb0-853d-73b55f4e7bff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "POOLHOUSE\n"
     ]
    }
   ],
   "source": [
    "place_up= place.upper() #changes the lower case to upper, DIFFERENT METHODS\n",
    "print(place_up)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a2962122-2b88-49ad-a0aa-b07c9070f716",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "poolhouse\n"
     ]
    }
   ],
   "source": [
    "place_down = place.lower()\n",
    "print(place_down)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8314375d-2c02-49fc-965e-eea3478b7abe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "place.count(\"o\") #counts the number of o's in the word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "7c9a5f6e-409d-4e3f-8758-c04abfea60c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "areas = [11.25, 18.0, 20.0, 10.75, 9.50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3c43c873-8370-42f6-b9e8-a47605e0046e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "areas.index(20.0) #shows the index number of the element"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "996df5d3-b32f-425c-a5ae-67efe06d28d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "areas.count(9.50) #shows the frequency of element in a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "c04663fc-be11-42a5-ace5-c32e589ec55a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "areas.index(20.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "c8c07779-cd28-4088-980f-064643374892",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.0"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "areas[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "92c0c818-28cb-40ba-b9c5-c485c34fd1cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "areas = [11.25, 18.0, 20.0, 10.75, 9.50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "4759dd85-a4dd-43d6-9f60-ce2fe630e173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45, 24.5, 15.45]\n"
     ]
    }
   ],
   "source": [
    "areas.append(24.5) #adds elements to the list\n",
    "areas.append(15.45)\n",
    "print(areas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "f7776877-2e6e-4f4a-969c-fcd5cf085a5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45, 24.5, 15.45]\n"
     ]
    }
   ],
   "source": [
    "areas.reverse() #reverses the order of the elements in the list\n",
    "print(areas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "6186eccd-ff1b-4a87-abe7-9f88e36ed54d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "import math as mt #import all the functions within the math package, the as word allows to localize the function\n",
    "d= mt.pi \n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "7e953ff2-1d1c-4172-9ab7-de18414a7f69",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import radians #only imports a specific function\n",
    "from math import pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "a47fde13-ee4c-41a3-8e82-f8e3fe6c73a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#things will be fine and wonderful"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "47a769c8-5273-4842-af61-d0cb526c49c3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'positions' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[63], line 5\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;66;03m# Convert positions and heights to numpy arrays: np_positions, np_heights\u001b[39;00m\n\u001b[0;32m----> 5\u001b[0m np_positions \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray(positions)\n\u001b[1;32m      6\u001b[0m np_heights \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray(heights)\n\u001b[1;32m     10\u001b[0m \u001b[38;5;66;03m# Heights of the goalkeepers: gk_heights\u001b[39;00m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'positions' is not defined"
     ]
    }
   ],
   "source": [
    "## Import numpy\n",
    "import numpy as np\n",
    "\n",
    "# Convert positions and heights to numpy arrays: np_positions, np_heights\n",
    "np_positions = np.array(positions)\n",
    "np_heights = np.array(heights)\n",
    "\n",
    "\n",
    "\n",
    "# Heights of the goalkeepers: gk_heights\n",
    "\n",
    "gk_heights = np_heights[np_positions =='GK']\n",
    "\n",
    "# Heights of the other players: other_heights\n",
    "other_heights = np_heights[np_positions!='GK']\n",
    "\n",
    "# Print out the median height of goalkeepers. Replace 'None'\n",
    "print(\"Median height of goalkeepers: \" + str(np.median(gk_heights)))\n",
    "\n",
    "# Print out the median height of other players. Replace 'None'\n",
    "print(\"Median height of other players: \" + str(np.median(other_heights)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "6cb09fd7-93c0-4e23-93aa-d312e07867cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "year = [1970, 1980, 1990, 2000, 2010, 2020]\n",
    "pop = [2.564, 3.530, 5.980, 6.528, 7.409, 8.098]\n",
    "plt.plot(year, pop)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "d8261e6d-1e06-4da7-ae6a-557651322c9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020\n",
      "8.098\n"
     ]
    }
   ],
   "source": [
    "print(year[-1]) #the last element within year\n",
    "print(pop[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "1e129284-8218-4da2-88af-b85dd45156a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ud1uRUVF+SyLiIjwTo4GztbIXqnqklJHzgBdOdphSdf2SFHvVhwKAwCc3lkdDjPGaNSoUYqOjvYuO3bsmMaOHav4+Hjvsnnz5gWuQtRoToelp6/prMueX6afi0tUmTnSToelZvXi9MDQdoErEABQY51VCLrxxhvLLBs5cmTAioE9Na8fr9m39NJ1M77WkeNuuf1IQk5LalYvVm/e2ku1YyKDUCUAoKaxjDHBuXlTFVJQUCCXy6X8/HwlJCSEuxycQvbBIk18a41W7zxU4fdYlmSMdFmnxnr48vaqExd15jcBAKqFYP9++3WxRCAYmiXGae5t52v2imy9tGSrdh06qgiHVeY6QpYkh8OS22N0bnKCJlx4ji46t2F4igYAVFvsCUKV5PEYLfvxgJb9eEBrcw5r608/67jbo9gIp9omJ6hTU5cGt2uoTil1wl0qACBI2BMEW3I4LF1wTgNdcE6DcJcCAKih/LqBKgAAQHVHCAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALZECAIAALYUEe4CqqPDRce1fne+tv10RCfcHiXERKpdcoLaNKqtqAhyJQAA1QEhqIKMMVq8+Se98uV2LdtyQEaSZUmWJI85uU5clFO/756im/o0V2pifDjLBQAAZ2AZY0y4iwi2goICuVwu5efnKyEh4azfv7/wmP7fvA36dNM+OR2W3J5TD5nTYclhSZN+01Y39Wkhp8OqTOkAANhWZX+/z4Q9QWew48AR/f7l5Tp45LgknTYAlb7uljT5g01ak3NYz1zTWRFODpEBAFDV8Ot8GoeLjuva6V/r4JHjZww/5flg3V79z7vfBaEyAABQWYSg0/jf977TT4XH/ApAkmQkzV6RrcWb9we2MAAAUGmEoFPIyj6k+Wv2yF3JGVMOS/rz/A3y+BmkAABAcBCCTuH15TsDMqnZY6Rdh45q6Y8HAlAVAAAIFEJQOdweo4827PX7MNivOR2WPlq/NyBtAQCAwCAElWP7gZ917IQnYO25PUZZ2YcD1h4AAKg8QlA5dh4sCnib2YcC3yYAAPAfIagcgToM9ktMjAYAoGohBJWjXnxUwNusExcZ8DYBAID/CEHlaJecoEDe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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np_pop = np.array(pop)\n",
    "np_pop = np_pop*80\n",
    "plt.scatter(year, pop, s =np_pop)\n",
    "plt.xscale(\"log\")\n",
    "\n",
    "plt.xlabel(\"Year\") #shows the title of the x axis\n",
    "plt.ylabel(\"Population\") #shows the title of the y axis\n",
    "plt.title(\"World Development\") #shows the overall title of the graph\n",
    "ticks = (0,2,4,6,8) #the first tick\n",
    "ticks_a = (0, \"2B\", \"4B\", \"6B\", \"8B\") #the tick we want as new replacements\n",
    "plt.yticks(ticks, ticks_a) #the changes to the y axis, B representing billions\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "0f2674be-a9bb-4bcc-8931-323a9f32c53b",
   "metadata": {},
   "outputs": [],
   "source": [
    "countries = ['spain', 'france', 'germany', 'norway']\n",
    "capitals = ['madrid', 'paris', 'berlin', 'oslo']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "3c81bcb9-21fc-4916-bf25-36b25f94a19a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "berlin\n"
     ]
    }
   ],
   "source": [
    "# Get index of 'germany': ind_ger\n",
    "ind_ger = countries.index('germany')\n",
    "# Use ind_ger to print out capital of Germany\n",
    "print(capitals[ind_ger])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "d410b2ab-c5a9-4cea-8af3-2af42c179d15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['spain', 'france', 'germany', 'norway'])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' } #the dictionary\n",
    "europe.keys() #the different keys within the dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "ddf90000-efff-4d49-b768-d4be95da1d42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'oslo'"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "europe['norway']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "7753f51b-0cb0-4113-bba9-1f185397eb4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'sealand' in europe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "0ed7c038-0e9a-4359-8cf0-c195e63caf30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'sealand': 2.8e-05}\n"
     ]
    }
   ],
   "source": [
    "europe['sealand'] = 0.000028 #the sealand is being added to the dictionary\n",
    "print(europe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "e6989492-1f02-4470-89a7-8fda3990cbba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}\n"
     ]
    }
   ],
   "source": [
    "del(europe['sealand']) #the sealand is being deleted\n",
    "print(europe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "ad566feb-5993-4e86-bfed-7b46d3cdeb32",
   "metadata": {},
   "outputs": [],
   "source": [
    "europe = { 'spain': { 'capital':'madrid', 'population':46.77 },\n",
    "           'france': { 'capital':'paris', 'population':66.03 },\n",
    "           'germany': { 'capital':'berlin', 'population':80.62 },\n",
    "           'norway': { 'capital':'oslo', 'population':5.084 } }\n",
    "#here is a dictionary within a dictionary\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "944b7811-7e5b-44fb-8b3b-a9e101e5da38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "berlin\n"
     ]
    }
   ],
   "source": [
    "print(europe['germany']['capital']) #here I extracted the capital of germany using chained square bracket"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "0a4bc86d-5111-4b92-951f-9bc66340bd97",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'capital': 'rome', 'population': 59.83}\n",
    "#creating sub-dict data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "a18c2776-caa3-4bd6-ad1c-5e8c18316978",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'italy': {'capital': 'rome', 'population': 59.83}}\n"
     ]
    }
   ],
   "source": [
    "europe['italy'] = data\n",
    "#Add data to europe under key 'italy'\n",
    "print(europe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "51e25964-ea0f-4a23-bec4-8a68756437ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pre-defined lists\n",
    "names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']\n",
    "dr =  [True, False, False, False, True, True, True]\n",
    "cpc = [809, 731, 588, 18, 200, 70, 45]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "a0fbe734-7b6e-4d88-9f61-d7b997562c5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         country  drives_right  cars_per_cap\n",
      "0  United States          True           809\n",
      "1      Australia         False           731\n",
      "2          Japan         False           588\n",
      "3          India         False            18\n",
      "4         Russia          True           200\n",
      "5        Morocco          True            70\n",
      "6          Egypt          True            45\n"
     ]
    }
   ],
   "source": [
    "# Import pandas as pd\n",
    "\n",
    "import pandas as pd\n",
    "# Create dictionary my_dict with three key:value pairs: my_dict\n",
    "\n",
    "my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}\n",
    "# Build a DataFrame cars from my_dict: cars\n",
    "\n",
    "cars = pd.DataFrame(my_dict)\n",
    "# Print cars\n",
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "03f393ff-befc-43c7-acff-fcd2573d7edc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           country  drives_right  cars_per_cap\n",
      "US   United States          True           809\n",
      "AUS      Australia         False           731\n",
      "JPN          Japan         False           588\n",
      "IN           India         False            18\n",
      "RU          Russia          True           200\n",
      "MOR        Morocco          True            70\n",
      "EG           Egypt          True            45\n"
     ]
    }
   ],
   "source": [
    "# Definition of row_labels\n",
    "row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']\n",
    "\n",
    "# Specify row labels of cars, the columns starts from row_labels as opposed to numbers\n",
    "cars.index = row_labels\n",
    "\n",
    "# Print cars again\n",
    "print(cars)\n",
    "\n",
    "\n",
    "##Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "e0a7e5a8-e330-46b0-b3f5-7b6540bf9c40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         country  drives_right  cars_per_cap\n",
      "0  United States          True           809\n",
      "1      Australia         False           731\n",
      "2          Japan         False           588\n",
      "3          India         False            18\n",
      "4         Russia          True           200\n",
      "5        Morocco          True            70\n",
      "6          Egypt          True            45\n"
     ]
    }
   ],
   "source": [
    "# Import pandas as pd\n",
    "\n",
    "import pandas as pd\n",
    "# Create dictionary my_dict with three key:value pairs: my_dict\n",
    "\n",
    "my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}\n",
    "# Build a DataFrame cars from my_dict: cars\n",
    "\n",
    "cars = pd.DataFrame(my_dict)\n",
    "# Print cars\n",
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "32142cd3-dd7e-4e9c-ae44-6cedd9144664",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. square brackets \n",
    "#column access. Row access but through slicing\n",
    "#2. loc(label-based)\n",
    "#row access  => brics.loc[[\"a\", \"v\", \"c\"]]\n",
    "#column access => brics.loc[:, [\"a\", \"ad\"]]\n",
    "#bric.iloc[[1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "f469d0f9-a3c2-4ab2-a283-f03531db4973",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    United States\n",
      "1        Australia\n",
      "2            Japan\n",
      "3            India\n",
      "4           Russia\n",
      "5          Morocco\n",
      "6            Egypt\n",
      "Name: country, dtype: object\n",
      "         country\n",
      "0  United States\n",
      "1      Australia\n",
      "2          Japan\n",
      "3          India\n",
      "4         Russia\n",
      "5        Morocco\n",
      "6          Egypt\n",
      "         country  drives_right\n",
      "0  United States          True\n",
      "1      Australia         False\n",
      "2          Japan         False\n",
      "3          India         False\n",
      "4         Russia          True\n",
      "5        Morocco          True\n",
      "6          Egypt          True\n"
     ]
    }
   ],
   "source": [
    "# Print out country column as Pandas Series\n",
    "\n",
    "print(cars[\"country\"])\n",
    "# Print out country column as Pandas DataFrame\n",
    "print(cars[[\"country\"]])\n",
    "# Print out DataFrame with country and drives_right columns\n",
    "\n",
    "print(cars[[\"country\", \"drives_right\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "2850ab57-e9e2-4e1a-b62a-58b860aa193b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     country  drives_right  cars_per_cap\n",
      "1  Australia         False           731\n",
      "2      Japan         False           588\n",
      "  country  drives_right  cars_per_cap\n",
      "3   India         False            18\n",
      "4  Russia          True           200\n"
     ]
    }
   ],
   "source": [
    "print(cars[1:3])\n",
    "print(cars[3:5]) #showing the observation with index number 3 to five"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48cafda1-0fde-4105-9e6a-c59de4434142",
   "metadata": {},
   "source": [
    "#loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "15d941c6-d521-4816-869c-4d188b52ee4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country         Russia\n",
       "drives_right      True\n",
       "cars_per_cap       200\n",
       "Name: 4, dtype: object"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.iloc[4] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "9f046a8e-2463-40af-8d71-7d6e09c4bd4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>drives_right</th>\n",
       "      <th>cars_per_cap</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Australia</td>\n",
       "      <td>False</td>\n",
       "      <td>731</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>India</td>\n",
       "      <td>False</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     country  drives_right  cars_per_cap\n",
       "1  Australia         False           731\n",
       "3      India         False            18"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.loc[[1, 3]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "0375f224-cbfe-4c70-9a7f-9dcdb3e73348",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   drives_right\n",
      "0          True\n",
      "1         False\n",
      "2         False\n",
      "3         False\n",
      "4          True\n",
      "5          True\n",
      "6          True\n"
     ]
    }
   ],
   "source": [
    "# Print out drives_right column as Series\n",
    "\n",
    "print(cars.loc[:, [\"drives_right\"]])\n",
    "# Print out drives_right column as DataFrame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "e3037242-7187-470b-acad-6835c29d75e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   drives_right\n",
      "0          True\n",
      "1         False\n",
      "2         False\n",
      "3         False\n",
      "4          True\n",
      "5          True\n",
      "6          True\n"
     ]
    }
   ],
   "source": [
    "# Print out drives_right column as DataFrame\n",
    "print(cars.loc[:, [\"drives_right\"]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "81892470-82f7-4a4c-9555-ddf036e24e65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   cars_per_cap  drives_right\n",
      "0           809          True\n",
      "1           731         False\n",
      "2           588         False\n",
      "3            18         False\n",
      "4           200          True\n",
      "5            70          True\n",
      "6            45          True\n"
     ]
    }
   ],
   "source": [
    "# Print out cars_per_cap and drives_right as DataFrame\n",
    "\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "c48d0b01-db46-4e96-b3eb-3ed2e95aa903",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Comparison of booleans\n",
    "print(True == False)\n",
    "\n",
    "# Comparison of integers\n",
    "\n",
    "print(-5*15!=75)\n",
    "# Comparison of strings\n",
    "\n",
    "print(\"pyscript\"==\"PyScript\")\n",
    "# Compare a boolean with an integer\n",
    "\n",
    "print(True == 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "d92668c5-e069-480c-86b9-c22d5f74b6d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(True>False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "6c62cfb2-0f5d-49d5-b697-354007a8a663",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Comparison of integers\n",
    "x = -3 * 6\n",
    "\n",
    "print(-10<=x)\n",
    "# Comparison of strings\n",
    "y = \"test\"\n",
    "\n",
    "print(y>=\"test\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "26fc0d10-4993-4bbe-841c-5777518a149d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True  True False False]\n",
      "[False  True  True False]\n"
     ]
    }
   ],
   "source": [
    "my_house = np.array([18.0, 20.0, 10.75, 9.50])\n",
    "your_house = np.array([14.0, 24.0, 14.25, 9.0])\n",
    "\n",
    "# my_house greater than or equal to 18\n",
    "\n",
    "print(18<=my_house)\n",
    "# my_house less than your_house\n",
    "print(my_house<your_house)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "2c5e5a13-83e5-4843-b6a3-b1c447949a2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Define variables\n",
    "my_kitchen = 18.0\n",
    "your_kitchen = 14.0\n",
    "\n",
    "# my_kitchen bigger than 10 and smaller than 18?\n",
    "\n",
    "print(my_kitchen>10 and my_kitchen<18)\n",
    "# my_kitchen smaller than 14 or bigger than 17?\n",
    "\n",
    "print(my_kitchen<14 or my_kitchen>17)\n",
    "# Double my_kitchen smaller than triple your_kitchen?\n",
    "print(my_kitchen*2 < your_kitchen*3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "083db10f-f047-483c-b79b-822c8beb93ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 10\n",
    "y = 18\n",
    "z = 8\n",
    "x<10 and y>19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "d7f3c74f-3e10-4810-b116-2d193fb426a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x ==10 and y ==18 #True and True is True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "79999f2f-6766-440d-9a29-0da64a374c55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x>9 and z<7 #True and False is False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "8c9dcb86-c587-4ee2-9ebb-089e718cb4bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x>18 and y<19 #False and False is False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "181b21f3-18d2-4227-9678-72506c753f77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x == 10 or y == 8 #True or False is True "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "6e63fb5e-3442-4da4-9ac9-25f513725e28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x<7 or z >9 #False or false is false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "ca6edfe7-42f1-4f43-b9f9-9673cca76ccd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 8 #not is executed first\n",
    "y = 9\n",
    "\n",
    "not(not(x<3) and not(y>14 or y>10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "7cc404ce-9b8b-4f84-ab87-4882173a6737",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True  True  True  True]\n",
      "[False False False  True]\n"
     ]
    }
   ],
   "source": [
    "my_house = np.array([18.0, 20.0, 10.75, 9.50])\n",
    "your_house = np.array([14.0, 24.0, 14.25, 9.0])\n",
    "\n",
    "# my_house greater than 18.5 or smaller than 10\n",
    "print(np.logical_or(my_house>13, your_house<15))\n",
    "\n",
    "# Both my_house and your_house smaller than 11\n",
    "print(np.logical_and(my_house <11, your_house<11))\n",
    "\n",
    "#we need np.logical_and(), np.logical_or, and np.logical_not to use (not, and, and or) with numpy arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "cbae0430-61b8-4214-a1a1-b74500373ea5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "p is: 2\n"
     ]
    }
   ],
   "source": [
    "p = 2\n",
    "q = \"p is: \"\n",
    "print(q+str(p))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "52b015ec-5109-4890-a961-4f8298896294",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pythondata'"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"python\" + \"data\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "4aa0b490-20e7-4699-8699-9ca62f781f97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "looking around in the kitchen.\n",
      "pretty small.\n"
     ]
    }
   ],
   "source": [
    "# Define variables\n",
    "room = \"kit\"\n",
    "area = 14.0\n",
    "\n",
    "# if-else construct for room\n",
    "if room == \"kit\" :\n",
    "    print(\"looking around in the kitchen.\")\n",
    "else :\n",
    "    print(\"looking around elsewhere.\")\n",
    "\n",
    "# if-else construct for area\n",
    "if area > 15 :\n",
    "    print(\"big place!\")\n",
    "else :\n",
    "    print(\"pretty small.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "96222cf4-7473-402c-b5ef-b8f0e0af961e",
   "metadata": {},
   "outputs": [],
   "source": [
    "row_labels = (\"US\", \"AU\", \"JA\", \"IN\", \"RU\", \"MO\", \"EG\")\n",
    "cars.index=row_labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "a564a2c9-b681-4d39-858e-1c68ecea4659",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          country  drives_right  cars_per_cap\n",
      "US  United States          True           809\n",
      "RU         Russia          True           200\n",
      "MO        Morocco          True            70\n",
      "EG          Egypt          True            45\n"
     ]
    }
   ],
   "source": [
    "# Extract drives_right column as Series: dr\n",
    "dr = cars[\"drives_right\"]\n",
    "\n",
    "# Use dr to subset cars: sel\n",
    "sel = cars[dr]\n",
    "\n",
    "# Print sel\n",
    "print(sel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "0ab3ba19-ab7b-4bc5-8d36-35eb385f5ca6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          country  drives_right  cars_per_cap\n",
      "US  United States          True           809\n",
      "AU      Australia         False           731\n",
      "JA          Japan         False           588\n",
      "IN          India         False            18\n",
      "RU         Russia          True           200\n",
      "MO        Morocco          True            70\n",
      "EG          Egypt          True            45\n"
     ]
    }
   ],
   "source": [
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "7e1f28ec-023f-462c-852d-3260d3f807e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   country  drives_right  cars_per_cap\n",
      "RU  Russia          True           200\n"
     ]
    }
   ],
   "source": [
    "# Create medium: observations with cars_per_cap between 100 and 500\n",
    "\n",
    "cpc = cars['cars_per_cap']\n",
    "between = np.logical_and(cpc > 100, cpc < 500)\n",
    "medium = cars[between]\n",
    "\n",
    "\n",
    "# Print medium\n",
    "print(medium)\n",
    "\n",
    "#Russia has cars between 100 and 500"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "e5f7e345-91a0-4e70-96ba-c214152a0c2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          country  drives_right  cars_per_cap\n",
      "US  United States          True           809\n",
      "AU      Australia         False           731\n",
      "JA          Japan         False           588\n"
     ]
    }
   ],
   "source": [
    "# Create car_maniac: observations that have a cars_per_cap over 500\n",
    "cpc = cars[\"cars_per_cap\"]\n",
    "\n",
    "many_cars = cpc>500\n",
    "\n",
    "car_maniac = cars[many_cars]\n",
    "# Print car_maniac\n",
    "print(car_maniac)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "4f63477f-9241-4b89-b6b0-940446b22002",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "correcting...\n",
      "7\n",
      "correcting...\n",
      "6\n",
      "correcting...\n",
      "5\n",
      "correcting...\n",
      "4\n",
      "correcting...\n",
      "3\n",
      "correcting...\n",
      "2\n",
      "correcting...\n",
      "1\n",
      "correcting...\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Initialize offset\n",
    "offset = 8\n",
    "while offset != 0:\n",
    "    print(\"correcting...\")\n",
    "    offset = offset - 1\n",
    "    print(offset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "fd8db02e-561c-481e-9dde-4ab91dc7536b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "x = 1\n",
    "while x < 4 :\n",
    "    print(x)\n",
    "    x = x + 1\n",
    "\n",
    "#python keeps executing the code until the condition is false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42d3b631-2fd5-416d-96c2-e462eb2be474",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a186f8a-67bf-47d2-9ca8-f16dc0331c17",
   "metadata": {},
   "outputs": [],
   "source": [
    "# areas list\n",
    "areas = [11.25, 18.0, 20.0, 10.75, 9.50]\n",
    "\n",
    "# Code the for loop\n",
    "for rooms in areas :\n",
    "    print(rooms)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0466ebd7-bbfc-42e0-b2de-10d5febd86f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# areas list\n",
    "areas = [11.25, 18.0, 20.0, 10.75, 9.50]\n",
    "\n",
    "# Change for loop to use enumerate() and update print()\n",
    "for index, area in enumerate(areas) :\n",
    "    print(\"room \" + str(index) + \": \" + str(area))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5744f631-7508-4c63-9cff-b63a79656836",
   "metadata": {},
   "outputs": [],
   "source": [
    "# house list of lists\n",
    "house = [[\"hallway\", 11.25], \n",
    "         [\"kitchen\", 18.0], \n",
    "         [\"living room\", 20.0], \n",
    "         [\"bedroom\", 10.75], \n",
    "         [\"bathroom\", 9.50]]\n",
    "         \n",
    "# Build a for loop from scratch\n",
    "\n",
    "for room in house:\n",
    "    print(\"the \" + room[0] + \" is \" + str(room[1]) + \" sqm\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0ddf41b-d416-41bd-8c09-a08e1ef9a3aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definition of dictionary\n",
    "europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',\n",
    "          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }\n",
    "          \n",
    "# Iterate over europe\n",
    "for key, value in europe.items() :\n",
    "    print((\"The capital of \") + key + \" is \" + str(value)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d18bc004-6f18-45d7-aa8b-cd899151eb5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import cars data\n",
    "import pandas as pd\n",
    "cars = pd.read_csv('cars.csv', index_col = 0)\n",
    "\n",
    "# Use .apply(str.upper)\n",
    "cars[\"COUNTRY\"] = cars[\"country\"].apply(str.upper)\n",
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecfe1c66-6b9e-4384-b41b-d5f87baac0df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A DataFrame has a value, column index, and a row index\n",
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "159ccbea-ae81-4438-90bf-20ccc2ea7fad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "cars = pd.read.csv(\"TeslaInc.csv\")\n",
    "print(cars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c09b5f91-ad59-4129-9d15-bff4c982ba2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create indiv_per_10k col as homeless individuals per 10k state pop\n",
    "homelessness[\"indiv_per_10k\"] = 10000 * homelessness[\"individuals\"] / homelessness[\"state_pop\"] \n",
    "# Subset rows for indiv_per_10k greater than 20\n",
    "high_homelessness = homelessness[homelessness[\"indiv_per_10k\"]>20]\n",
    "\n",
    "# Sort high_homelessness by descending indiv_per_10k\n",
    "high_homelessness_srt = high_homelessness.sort_values(\"indiv_per_10k\", ascending=False)\n",
    "\n",
    "# From high_homelessness_srt, select the state and indiv_per_10k cols\n",
    "result = high_homelessness_srt[[\"state\", \"indiv_per_10k\"]]\n",
    "\n",
    "# See the result\n",
    "print(result)\n",
    "\n",
    "\n",
    "# Add total col as sum of individuals and family_members\n",
    "homelessness[\"total\"] = homelessness[\"individuals\"]+homelessness[\"family_members\"]\n",
    "\n",
    "# Add p_individuals col as proportion of total that are individuals\n",
    "\n",
    "homelessness[\"p_individuals\"] = homelessness[\"individuals\"] / homelessness[\"total\"]\n",
    "# See the result\n",
    "print(homelessness)\n",
    "\n",
    "# Subset for rows in South Atlantic or Mid-Atlantic regions\n",
    "\n",
    "south_mid_atlantic = homelessness[(homelessness[\"region\"]==\"South Atlantic\") | (homelessness[\"region\"]==\"Mid-Atlantic\")]\n",
    "\n",
    "# See the result\n",
    "print(south_mid_atlantic)\n",
    "\n",
    "# Filter for rows where individuals is greater than 10000\n",
    "ind_gt_10k = homelessness[homelessness[\"individuals\"]>10000]\n",
    "\n",
    "# See the result\n",
    "print(ind_gt_10k)\n",
    "\n",
    "# Select the individuals column\n",
    "individuals = homelessness[\"individuals\"]\n",
    "\n",
    "\n",
    "# Print the head of the result\n",
    "print(individuals.head())\n",
    "\n",
    "# Sort homelessness by individuals\n",
    "\n",
    "homelessness_ind = homelessness.sort_values(\"individuals\", ascending=True )\n",
    "print(homelessness_ind.head())\n",
    "# Print the top few rows\n",
    "homelessness_ind.head()\n",
    "\n",
    "# Import pandas using the alias pd\n",
    "import pandas as pd\n",
    "\n",
    "# Print the values of homelessness\n",
    "print(homelessness.values)\n",
    "\n",
    "# Print the column index of homelessness\n",
    "print(homelessness.columns)\n",
    "# Print the row index of homelessness\n",
    "print(homelessness.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "96423bce-3200-4fe1-bd7a-e3da367fc6dc",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'sales' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# Drop duplicate store/type combinations\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m store_types \u001b[38;5;241m=\u001b[39m sales\u001b[38;5;241m.\u001b[39mdrop_duplicates([\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstore\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtype\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(store_types\u001b[38;5;241m.\u001b[39mhead())\n\u001b[1;32m      5\u001b[0m \u001b[38;5;66;03m# Drop duplicate store/department combinations\u001b[39;00m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'sales' is not defined"
     ]
    }
   ],
   "source": [
    "# Drop duplicate store/type combinations\n",
    "store_types = sales.drop_duplicates([\"store\", \"type\"])\n",
    "print(store_types.head())\n",
    "\n",
    "# Drop duplicate store/department combinations\n",
    "store_depts = sales.drop_duplicates(subset=[\"store\", \"department\"])\n",
    "print(store_depts.head())\n",
    "\n",
    "# Subset the rows where is_holiday is True and drop duplicate dates\n",
    "holiday_dates = sales[sales[\"is_holiday\"]].drop_duplicates(subset=\"date\")\n",
    "\n",
    "# Print date col of holiday_dates\n",
    "print(holiday_dates[\"date\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "85a7be1f-d6bf-43a4-9c8b-defc1a486636",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID     Name   Department  Salary\n",
      "0           1    Alice           HR   60000\n",
      "1           2      Bob  Engineering   80000\n",
      "2           3  Charlie    Marketing   75000\n",
      "3           4    David      Finance   65000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    'EmployeeID': [1, 2, 3, 4],\n",
    "    'Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Department': ['HR', 'Engineering', 'Marketing', 'Finance'],\n",
    "    'Salary': [60000, 80000, 75000, 65000]\n",
    "}\n",
    "\n",
    "# Create DataFrame\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8e791f3b-a7f8-44e9-a64a-cec9c2576083",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Salary\n",
      "Department          \n",
      "Engineering  80000.0\n",
      "Finance      65000.0\n",
      "HR           60000.0\n",
      "Marketing    75000.0\n"
     ]
    }
   ],
   "source": [
    "# Pivot for mean Salary for each Department type\n",
    "import numpy as np\n",
    "\n",
    "mean_salary_by_type = df.pivot_table(values=\"Salary\", index=\"Department\")\n",
    "\n",
    "# Print mean_sales_by_type\n",
    "print(mean_salary_by_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "45e7cadd-f132-4177-a041-897634b97941",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name           Alice      Bob  Charlie    David\n",
      "Department                                     \n",
      "Engineering      0.0  80000.0      0.0      0.0\n",
      "Finance          0.0      0.0      0.0  65000.0\n",
      "HR           60000.0      0.0      0.0      0.0\n",
      "Marketing        0.0      0.0  75000.0      0.0\n"
     ]
    }
   ],
   "source": [
    "# Print mean salary by department and Name; fill missing values with 0\n",
    "print(df.pivot_table(values=\"Salary\", index=\"Department\", columns =\"Name\", fill_value=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fff44cbf-5c6a-4209-a0a3-3a74b22c0249",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name           Alice      Bob  Charlie    David      All\n",
      "Department                                              \n",
      "Engineering      9.0  80000.0      9.0      9.0  80000.0\n",
      "Finance          9.0      9.0      9.0  65000.0  65000.0\n",
      "HR           60000.0      9.0      9.0      9.0  60000.0\n",
      "Marketing        9.0      9.0  75000.0      9.0  75000.0\n",
      "All          60000.0  80000.0  75000.0  65000.0  70000.0\n"
     ]
    }
   ],
   "source": [
    "# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols\n",
    "print(df.pivot_table(values=\"Salary\", index=\"Department\", columns=\"Name\", fill_value =9, margins = True))\n",
    "\n",
    "#fill_value fills the missing value with a number\n",
    "#margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: \n",
    "#it gives the row and column totals of the pivot table contents."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "084eee65-d67c-4d91-921d-0cf8a5323e9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID     Name   Department  Salary\n",
      "0           1    Alice           HR   60000\n",
      "1           2      Bob  Engineering   80000\n",
      "2           3  Charlie    Marketing   75000\n",
      "3           4    David      Finance   65000\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fd4f31d4-3fac-4dd6-9624-1b1af0d06183",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Name   Department  Salary\n",
      "EmployeeID                              \n",
      "1             Alice           HR   60000\n",
      "2               Bob  Engineering   80000\n",
      "3           Charlie    Marketing   75000\n",
      "4             David      Finance   65000\n"
     ]
    }
   ],
   "source": [
    "df_ind = df.set_index(\"EmployeeID\")\n",
    "print(df_ind)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8ebb57c2-644d-4bb3-a0e0-6b664f0d0399",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   index  EmployeeID     Name   Department  Salary\n",
      "0      0           1    Alice           HR   60000\n",
      "1      1           2      Bob  Engineering   80000\n",
      "2      2           3  Charlie    Marketing   75000\n",
      "3      3           4    David      Finance   65000\n"
     ]
    }
   ],
   "source": [
    "print(df.reset_index()), #undoes the setting of index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "26ddb7d5-d68f-4dac-9c21-3a110999d103",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID     Name   Department  Salary\n",
      "0           1    Alice           HR   60000\n",
      "1           2      Bob  Engineering   80000\n",
      "2           3  Charlie    Marketing   75000\n",
      "3           4    David      Finance   65000\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(None,)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(df.reset_index(drop=True)) #drops the index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "e6acde7d-a3c8-4197-9367-591843fd13b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get 23rd row, 2nd column (index 22, 1)\n",
    "print(temperatures.iloc[22:1, :])\n",
    "\n",
    "# Use slicing to get the first 5 rows\n",
    "print(temperatures.iloc[:5])\n",
    "\n",
    "# Use slicing to get columns 3 to 4\n",
    "print(temperatures.iloc[:, 2:4])\n",
    "\n",
    "# Use slicing in both directions at once\n",
    "print(temperatures.iloc[:5, 2:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "95024941-52d1-4e30-ab26-a48a7c3ae639",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID     Name   Department  Salary\n",
      "0           1    Alice           HR   60000\n",
      "1           2      Bob  Engineering   80000\n",
      "2           3  Charlie    Marketing   75000\n",
      "3           4    David      Finance   65000\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0b7136b8-52d2-4b24-ba6e-cce884f07dab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Name   Department  Salary\n",
      "1  Bob  Engineering   80000\n"
     ]
    }
   ],
   "source": [
    "print(df.iloc[1:2, 1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7b1bc300-1ff6-4e56-9229-a2c11dbcb330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID     Name   Department  Salary\n",
      "0           1    Alice           HR   60000\n",
      "1           2      Bob  Engineering   80000\n",
      "2           3  Charlie    Marketing   75000\n",
      "3           4    David      Finance   65000\n",
      "4           5    Samir           IT     999\n"
     ]
    }
   ],
   "source": [
    "#line graphs visualizing numeric data over time\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    'EmployeeID': [1, 2, 3, 4, 5],\n",
    "    'Name': ['Alice', 'Bob', 'Charlie', 'David', \"Samir\"],\n",
    "    'Department': ['HR', 'Engineering', 'Marketing', 'Finance', \"IT\"],\n",
    "    'Salary': [60000, 80000, 75000, 65000, 999]\n",
    "}\n",
    "\n",
    "# Create DataFrame\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "42d53c93-cec8-4146-8dbf-859abb31840f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   EmployeeID   Name  Department  Salary\n",
      "0       False  False       False   False\n",
      "1       False  False       False   False\n",
      "2       False  False       False   False\n",
      "3       False  False       False   False\n",
      "4       False  False       False   False\n",
      "EmployeeID    0\n",
      "Name          0\n",
      "Department    0\n",
      "Salary        0\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "image/png": "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qjoBAADaJKgFxcuXL9f69et14sQJZWdna+PGjcrOzta3vnU5KyUnJ2vt2rW67bbbQlosAADA9QQVbtasWaNZs2Zp5syZ6t27d6t9+vXrp+Li4hsqDgAAIFBBhZur/WDe10VFRWnGjBnBvD0AAEDQglpzs379er388sst2l9++WW9+OKLN1wUAABAsIIKN0uXLlXPnj1btMfHx+s//uM/brgoAACAYAUVbs6cOdPqoxL69+/v94N7AAAAHS2ocBMfH6/33nuvRfu7776rHj163HBRAAAAwQoq3Dz00EOaO3euysrK1NTUpKamJu3du1fz5s3TQw89FOoaAQAA2iyou6X+/d//XWfOnFFmZqYiIi6/RXNzs6ZPn86aGwAAYKugwk1UVJS2bt2qX//613r33XfVtWtX3X777erfv3+o6wMAAAhIUOHmiiFDhmjIkCGhqgUAAOCGBRVumpqatGHDBv35z39WXV2dmpub/V7fu3dvSIoDAAAIVFDhZt68edqwYYMmTpyoESNGyOFwhLouAACAoAQVbrZs2aI//OEPys7ODnU9AAAANySoW8GjoqI0aNCgUNcCAABww4IKN08++aSee+45WZYV6noAAABuSFCXpd544w2VlZVp165dSklJUWRkpN/r27ZtC0lxAAAAgQoq3HTv3l1TpkwJdS0AAAA3LKhws379+lDXAQAAEBJBrbmRpMbGRv33f/+31q5dqwsXLkiSzp07p4sXL4asOAAAgEAFdebmzJkz+vGPf6zq6mp5vV6NGzdOsbGx+s///E999dVXKioqCnWdAAAAbRLUmZt58+YpLS1Nn3/+ubp27eprnzJliv785z+HrDgAAIBABX231JtvvqmoqCi/9v79+6umpiYkhQEAAAQjqDM3zc3NampqatH+ySefKDY29oaLAgAACFZQ4WbcuHEqLCz07TscDl28eFHPPPMMj2QAAAC2Cuqy1O9//3uNHTtWw4cP11dffaWHH35YJ0+eVM+ePbV58+ZQ1wgAANBmQYWbPn366MiRI9q8ebMOHz6s5uZmzZ49W9OmTfNbYAwAANDRggo3ktS1a1fNmjVLs2bNCmU9AAAANySocLNx48Zrvj59+vSgigEAALhRQYWbefPm+e03NDToyy+/VFRUlG655RbCDQAAsE1Qd0t9/vnnftvFixd14sQJ3XPPPSwoBgAAtgr6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mqqYmBgNHDhQRUVFHVRp5xbIPG/btk3jxo1Tr169FBcXp/T0dP3pT3/qwGo7t0D/TF/x5ptvKiIiQt/73vfat8BOiHBzE3r44Yd15MgR7d69W7t379aRI0eUk5PTprGvvfaa/vKXv7Tp569vdoHO85dffqnDhw/r3/7t33T48GFt27ZNH330kX7yk590YNXhbevWrZo/f76efvppVVVVKSMjQxMmTPD7yYivO3XqlLKzs5WRkaGqqiotXrxYc+fOVUlJSQdX3rkEOs/79+/XuHHjtHPnTh06dEhjx47VpEmTVFVV1cGVdz6BzvUVbrdb06dPV2ZmZgdV2slYuKl8+OGHliTr4MGDvraKigpLknX8+PFrjv3kk0+s7373u9b7779v9e/f3/r973/fztV2Xjcyz1/39ttvW5KsM2fOtEeZnc5dd91l5ebm+rXddttt1qJFi1rt/4tf/MK67bbb/Noee+wxa/To0e1WowkCnefWDB8+3FqyZEmoSzNOsHP94IMPWv/6r/9qPfPMM9Ydd9zRjhV2Tpy5uclUVFTI6XTqBz/4ga9t9OjRcjqdeuutt646rrm5WTk5OfqXf/kXpaSkdESpnVqw8/xNbrdbDoeD56FJqq+v16FDh5SVleXXnpWVddU5raioaNF//PjxqqysVENDQ7vV2pkFM8/f1NzcrAsXLujWW29tjxKNEexcr1+/Xh9//LGeeeaZ9i6x07L9qeDoWLW1tYqPj2/RHh8f3+KhpF/329/+VhEREZo7d257lmeMYOf567766istWrRIDz/8MA/Mk3T+/Hk1NTW1eLBuQkLCVee0tra21f6NjY06f/68EhMT263eziqYef6m3/3ud7p06ZJ++tOftkeJxghmrk+ePKlFixbpwIEDiojgK/xqOHNjiF/+8pdyOBzX3CorKyVJDoejxXjLslptl6RDhw7pueee04YNG67a52bRnvP8dQ0NDXrooYfU3Nys1atXh/w4OrNvzt/15rS1/q21w1+g83zF5s2b9ctf/lJbt25tNeCjpbbOdVNTkx5++GEtWbJEQ4YM6ajyOiVinyEef/xxPfTQQ9fsM2DAAL333nv69NNPW7z2v//7vy3+93DFgQMHVFdXp379+vnampqa9OSTT6qwsFCnT5++odo7k/ac5ysaGhr005/+VKdOndLevXs5a/N/evbsqS5durT4H21dXd1V57R3796t9o+IiFCPHj3ardbOLJh5vmLr1q2aPXu2Xn75Zf3oRz9qzzKNEOhcX7hwQZWVlaqqqtLjjz8u6fIlQMuyFBERoT179ui+++7rkNrDHeHGED179lTPnj2v2y89PV1ut1tvv/227rrrLknSX/7yF7ndbt19992tjsnJyWnxD9X48eOVk5OjmTNn3njxnUh7zrP0/4PNyZMnVVZWxhfw10RFRSk1NVWlpaWaMmWKr720tFT3339/q2PS09P1+uuv+7Xt2bNHaWlpioyMbNd6O6tg5lm6fMZm1qxZ2rx5syZOnNgRpXZ6gc51XFycjh496te2evVq7d27V6+88oqSk5PbveZOw8bFzLDJj3/8Y2vkyJFWRUWFVVFRYd1+++3WP/zDP/j1GTp0qLVt27arvgd3S11foPPc0NBg/eQnP7H69u1rHTlyxHK5XL7N6/XacQhhZ8uWLVZkZKRVXFxsffjhh9b8+fOtbt26WadPn7Ysy7IWLVpk5eTk+Pr/9a9/tW655RZrwYIF1ocffmgVFxdbkZGR1iuvvGLXIXQKgc7zSy+9ZEVERFirVq3y+3P7xRdf2HUInUagc/1N3C3VOsLNTeizzz6zpk2bZsXGxlqxsbHWtGnTrM8//9yvjyRr/fr1V30Pws31BTrPp06dsiS1upWVlXV4/eFq1apVVv/+/a2oqCjrzjvvtMrLy32vzZgxw7r33nv9+u/bt88aNWqUFRUVZQ0YMMBas2ZNB1fcOQUyz/fee2+rf25nzJjR8YV3QoH+mf46wk3rHJb1f6vrAAAADMDdUgAAwCiEGwAAYBTCDQAAMArhBgAAGIVwAwAAjEK4AQAARiHcAAAAoxBuAACAUQg3AADAKIQbAABgFMINAAAwCuEGAAAY5f8BO5jcOM3ER8AAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#the first thing in data analysis is knowing whether the dataset has missing values\n",
    "# Import matplotlib.pyplot with alias plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Check individual values for missing values\n",
    "print(df.isna())\n",
    "\n",
    "# Check each column for missing values\n",
    "print(df.isna().sum())\n",
    "\n",
    "# Bar plot of missing values by variable\n",
    "df.isna().sum().plot(kind=\"hist\")\n",
    "\n",
    "# Show plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "12e7f55b-84ab-4512-bf5f-3f72d9cb1f3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove rows with missing values\n",
    "#avocados_complete = avocados_2016.dropna()\n",
    "\n",
    "# Check if any columns contain missing values\n",
    "#print(avocados_complete.isna().any())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f7407a6e-4e97-4850-a149-de17b4558b51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         date  small_sold  large_sold\n",
      "0  2019-11-03    10376832     7835071\n",
      "1  2019-11-10    10717154     8561348\n"
     ]
    }
   ],
   "source": [
    "# Create a list of dictionaries with new data\n",
    "avocados_list = [\n",
    "    {\"date\": \"2019-11-03\", \"small_sold\": 10376832, \"large_sold\": 7835071},\n",
    "    {\"date\": \"2019-11-10\", \"small_sold\": 10717154, \"large_sold\": 8561348},\n",
    "]\n",
    "\n",
    "# Convert list into DataFrame\n",
    "avocados_2019 = pd.DataFrame(avocados_list)\n",
    "\n",
    "# Print the new DataFrame\n",
    "print(avocados_2019)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "52d7f6fc-1ccb-4928-a656-f799263f7469",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         date  small_sold  large_sold\n",
      "0  2019-11-17    10859987     7674135\n",
      "1  2019-12-01     9291631     6238096\n"
     ]
    }
   ],
   "source": [
    "# Create a dictionary of lists with new data\n",
    "avocados_dict = {\n",
    "  \"date\": [\"2019-11-17\", \"2019-12-01\"],\n",
    "  \"small_sold\": [10859987, 9291631],\n",
    "  \"large_sold\": [7674135, 6238096]\n",
    "}\n",
    "\n",
    "# Convert dictionary into DataFrame\n",
    "avocados_2019 = pd.DataFrame(avocados_dict)\n",
    "\n",
    "# Print the new DataFrame\n",
    "print(avocados_2019)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "56b9bf18-4270-459d-8aa0-4d6585ed4ebe",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'merge'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[23], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m date_merge \u001b[38;5;241m=\u001b[39m avocados_list\u001b[38;5;241m.\u001b[39mmerge(avocados_dict, on\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdate\u001b[39m\u001b[38;5;124m\"\u001b[39m, suffix \u001b[38;5;241m=\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moct\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnov\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'list' object has no attribute 'merge'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "date_merge = avocados_list.merge(avocados_dict, on=\"date\", suffix =(\"oct\", \"nov\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea023e78-f1b5-4428-a70d-7f90d98686cf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
