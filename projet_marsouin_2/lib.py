import time
def try_me() :
    print("Mon premier est la planète entre la Terre et Jupiter\n")
    time.sleep(2)
    print('Mon second est le cri que fait un nourisson\n')
    time.sleep(2)
    print('Mon tout est un animal aquatique de la famille des dauphins\n')
    time.sleep(2)
    print('Alors, quelle est ta réponse ?\n')
    rep = input()
    if 'marsouin' in rep :
        print('Bravo, tu as deviné correctement !')
    else :
        print('Et non, la bonne réponse était marsouin')