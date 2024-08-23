import time

def animatetext(text, timer):
    delay = timer / len(text)
    for i in text:
        print(i, end="", flush=True)
        time.sleep(delay)