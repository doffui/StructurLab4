import os
from collections import Counter
import time

def load_dict(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            return [x.strip() for x in f if x.strip()]
    except Exception as e:
        print(f"[!] Ошибка: {e}")
        return []

def process(words):
    d = {}
    lns = set()
    for w in words:
        ln = len(w)
        lns.add(ln)
        if ln not in d:
            d[ln] = []
        d[ln].append((w, Counter(w)))
    return d, sorted(lns, reverse=True)

def match(word, d, lst):
    c = Counter(word)
    res = []
    for l in lst:
        if l > len(word):
            continue
        for w, cnt in d[l]:
            if cnt <= c:
                res.append(w)
    return res

def run():
    print("Работу выполнила Захарова Анастасия Григорьевна 090301ПОВа-o24")
    file = 'nouns.txt'
    data = load_dict(file)
    if not data:
        print("[!] Словарь пуст или не найден.")
        return

    grouped, lengths = process(data)

    inp = input("Введите слово: ").strip()
    if not inp:
        print("[!] Ввод пустой.")
        return

    t0 = time.time()
    matches = match(inp, grouped, lengths)
    t1 = time.time()

    if matches:
        print("\nНайдены следующие слова:")
        for w in matches:
            print(w)
    else:
        print("\n[!] Ничего не найдено.")

    print(f"\nВремя выполнения: {t1 - t0:.4f} секунд")

if __name__ == "__main__":
    run()
