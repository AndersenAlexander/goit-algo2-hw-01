# main.py
from src.algorithms import min_max_divide_conquer, quick_select

if __name__ == "__main__":
    data = [12, -3, 7, 7, 42, 0, 5]
    mn, mx = min_max_divide_conquer(data)
    print(f"Divide & Conquer min/max of {data} -> ({mn}, {mx})")

    for k in range(1, len(data)+1):
        print(f"k={k}: {quick_select(data, k)}")
