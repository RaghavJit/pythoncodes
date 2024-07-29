import random
l=['a''b''c''d''e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    x=random.choice(l)
    print(x)
    y=input()
    print('')
    if y==x:
        continue
    else:
        break
