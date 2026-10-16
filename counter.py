import re
import sys
from collections import Counter

import matplotlib.pyplot as plt

TEXT = r"""Cinz wqvpv wrn cdgotzvgwts uixghxusvp cni pvsvhwxgj dptasv cxvsohxuqvip, Lvihlqnccp ovodhvo 
pxy puvhxcxh ivbdxivzvgwp: (1) wqv pfpwvzpqndso av, xc gnw wqvnivwxhtssf dgaivtltasv, 
dgaivtltasv xg uithwxhv; (2)hnzuinzxpv nc wqv pfpwvz pqndso gnw xghngkvgxvghv wqv 
hniivpungovgwp;(3) wqv lvf pqndso av ivzvzavitasv rxwqndw gnwvp tgo pqndso av 
vtpxsfhqtgjvtasv; (4) wqv hifuwnjitzp pqndso av witgpzxppxasv af wvsvjituq; (5)wqv tuutitwdp ni 
onhdzvgwp pqndso av uniwtasv tgo nuvitasv af t pxgjsvuvipng; (6) wqv pfpwvz pqndso av vtpf, 
gvxwqvi ivbdxixgj lgnrsvojv nc tsngj sxpw nc idsvp gni xgknskxgj zvgwts pwitxg.Wqvpv 
ivbdxivzvgwp pwxss hnzuixpv wqv xovts rqxhq zxsxwtif hxuqvip txztw. Wqvf qtkv avvg ivuqitpvo, 
tgo bdtsxwxvp wqtw sxv xzusxhxw qtkv -avvgztov vyusxhxw. Adw tgf znovig hifuwnjituqvi rndso 
av kvif qtuuf xc tgfhxuqvi cdscxssvo tss pxy.Nc hndipv, xw qtp gvkvi avvg unppxasv wn on wqtw. 
Wqviv tuuvtip wn av thviwtxg xghnzutwxaxsxwf tzngj wqvz wqtw ztlvp xw xzunppxasv wn 
xgpwxwdwvtss nc wqvz tw nghv. Wqv ivbdxivzvgw wqtw xp dpdtssf pthixcxhvo xp wqv 
cxipw.Lvihlqnccp tijdvo pwingjsf tjtxgpw wqv gnwxng nc t cxvso hxuqvi wqtw rndsopxzusf ivpxpw 
pnsdwxng sngj vgndjq cni wqv niovip xw witgpzxwwvo wn avhtiixvo ndw. Wqxp rtp gnw vgndjq, 
qv ptxo, ovhstixgj wqtw "wqv pvhivwztwwvi xg hnzzdgxhtwxngp pvgw nkvi t oxpwtghv kvif ncwvg 
ivwtxgp xwpxzuniwtghv avfngo wqv otf ng rqxhq xw rtp witgpzxwwvo." Qv rtp ng wqvpxov nc wqv 
tgjvsp, adw t uithwxhts cxvso hxuqvi wqtw xp dgaivtltasv rtpgnw unppxasv xg qxp otf, gni xp xw 
wnotf, tgo pn zxsxwtif hifuwnjituqf qtppvwwsvo cni cxvso hxuqvip wqtw ovstf adw on gnw ovcvtw 
hifuwtgtsfpxp.Uviqtup wqv znpw pwtiwsxgj ivbdxivzvgw, tw cxipw jstghv, rtp wqv pvhngo. 
Lvihlqnccp vyustxgvo wqtw af "pfpwvz" qv zvtgw "wqvztwvixts utiw nc wqv pfpwvz; wtasvtdy, 
hnov annlp, ni rqtwvkvizvhqtgxhts tuutitwdp ztf av gvhvpptif," tgo gnw "wqv lvf uinuvi."Lvihlqnccp 
qviv ztlvp cni wqv cxipw wxzv wqv oxpwxghwxng, gnr atpxh wnhifuwnsnjf, avwrvvg wqv jvgvits 
pfpwvz tgo wqv puvhxcxh lvf. Rqf zdpwwqv jvgvits pfpwvz "gnw ivbdxiv pvhivhf," tp, cni vytzusv, 
t hnovannlivbdxivp xw? Rqf zdpw xw av "t uinhvpp wqtw. . . ndi gvxjqanip htg vkvghnuf tgo tonuw"? 
Avhtdpv, Lvihlqnccp ptxo, "xw xp gnw gvhvpptif wnhngediv du xztjxgxgj uqtgwnzp tgo wn pdpuvhw 
wqv xghniiduwxaxsxwf ncvzusnfvvp ni pdatswvigp wn dgovipwtgo wqtw, xc t pfpwvz 
ivbdxixgjpvhivhf rviv xg wqv qtgop nc wnn stijv t gdzavi nc xgoxkxodtsp, xw hndsoav hnzuinzxpvo 
tw vthq vgjtjvzvgw xg rqxhq ngv ni tgnwqvi nc wqvzwnnl utiw." Wqxp qtp uinkvo wn av widv, tgo 
Lvihlqnccp' pvhngoivbdxivzvgw qtp avhnzv rxovsf thhvuwvo dgovi t cniz wqtw xp pnzvwxzvphtssvo 
wqv cdgotzvgwts tppdzuwxng nc zxsxwtif hifuwnjituqf: wqtw wqvvgvzf lgnrp wqv jvgvits pfpwvz. 
Adw qv zdpw pwxss av dgtasv wn pnskvzvpptjvp xg xw rxwqndw lgnrxgj wqv puvhxcxh lvf. Xg 
xwp znovigcnizdstwxng, wqv Lvihlqnccp onhwixgv pwtwvp wqtw pvhivhf zdpw ivpxovpnsvsf xg 
wqv lvfp.Qto Lvihlqnccp zvivsf udasxpqvo qxp uvihvuwxngp nc wqv uinasvzpcthxgj unpwwvsvjituq hifuwnjituqf tgo qxp uivphixuwxngp cni ivpnskxgjwqvz, qv rndso qtkv tppdivo t usthv cni 
qxzpvsc xg wqv utgwqvng nchifuwnsnjf. Adw qv oxo zniv. Qv hngwixadwvo t wvhqgxbdv nc 
hifuwtgtsfpxpwqtw xp nc pduivzv xzuniwtghv wnotf. Htssvo "pduvixzunpxwxng," 
xwhngpwxwdwvp wqv znpw jvgvits pnsdwxng cni unsftsuqtavwxh pdapwxwdwxngpfpwvzp. Rxwq 
cvr vyhvuwxngp, xw stfp gn ivpwixhwxngp ng wqv wfuv ni svgjwqnc lvfp, tp onvp wqv Ltpxplx 
zvwqno, gni ng wqv tsuqtavwp, rqxhq ztf avxgwviivstwvo ni vgwxivsf xgovuvgovgw. Xw rtgwp ngsf 
pvkvits zvpptjvp xgwqv ptzv lvf. Wqv hifuwtgtsfpw zdpw tsxjg wqvpv ngv tankv wqv nwqvi pnwqtw 
svwwvip vghxuqvivo rxwq wqv ptzv lvfsvwwvi rxss ctss xgwn t pxgjsvhnsdzg. Xg wqv pxzusvpw 
htpv, wqtw nc t idggxgj lvf (t kvif sngjhngwxgdndp wvyw dpvo tp t lvf, tp t gnkvs) wqtw ivpwtiwp 
rxwq vthqzvpptjv, qv htg on wqxp pxzusf af usthxgj tss wqv cxipw svwwvip xg wqv cxipwhnsdzg, 
tss wqv pvhngo svwwvip xg wqv gvyw hnsdzg, tgo pn ng"""

# Ciphertext in uppercase
CIPHER = TEXT.upper()

HELP = """
Commands:
  v=e          replace cipher letter V with E (several at once: v=e w=t q=h)
  -v           remove the substitution for cipher letter V
  map          show current substitutions
  freq         letter frequency table of the ciphertext
  chart        frequency chart
  reset        clear all substitutions
  show         show the text again
  help         this help
  stop         finish (also: empty line, exit, q)
"""


def letter_frequencies(text):
    """Counts letter frequencies (case-insensitive) and sorts them in descending order."""
    letters = [ch.lower() for ch in text if ch.isalpha()]
    return Counter(letters).most_common()


def print_table(freqs):
    total = sum(count for _, count in freqs)
    print(f"{'Letter':<8}{'Count':>8}{'Share':>9}  Chart")
    print("-" * 44)
    for letter, count in freqs:
        share = count / total * 100
        bar = "█" * max(1, round(share))
        print(f"{letter.upper():<8}{count:>8}{share:>8.1f}%  {bar}")
    print("-" * 44)
    print(f"{'Total':<8}{total:>8}")


def plot_chart(freqs):
    letters = [l.upper() for l, _ in freqs]
    counts = [c for _, c in freqs]

    plt.figure(figsize=(10, 5))
    plt.bar(letters, counts, color="#4C78A8")
    plt.title("Letter Frequencies in the Text")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("letter_freq.png", dpi=120)
    print("\nChart saved to letter_freq.png")
    plt.show()


def apply_mapping(text, mapping):
    """Replaces substituted letters with lowercase; unsolved ones stay uppercase."""
    return "".join(mapping.get(ch, ch) for ch in text)


def show_mapping(mapping):
    if not mapping:
        print("No substitutions yet.")
        return
    pairs = sorted(mapping.items())
    print("\nSubstitutions (cipher -> plain):")
    print("  " + "  ".join(f"{c}->{p}" for c, p in pairs))
    unused = sorted(set(c for c in CIPHER if c.isalpha()) - set(mapping))
    print("Not yet substituted: " + (" ".join(unused) if unused else "-"))


def process_command(cmd, mapping):
    """Handles one input line. Returns False when the user wants to stop."""
    cmd = cmd.strip()
    low = cmd.lower()

    if low in ("", "stop", "exit", "quit", "q"):
        return False
    if low == "help":
        print(HELP)
        return True
    if low == "map":
        show_mapping(mapping)
        return True
    if low == "freq":
        print_table(letter_frequencies(CIPHER))
        return True
    if low == "chart":
        plot_chart(letter_frequencies(CIPHER))
        return True
    if low == "reset":
        mapping.clear()
        print("All substitutions cleared.")
        return True
    if low == "show":
        return True

    for token in re.split(r"[,\s;]+", low):
        if not token:
            continue

        # Remove a substitution: -v
        m = re.fullmatch(r"-([a-z])", token)
        if m:
            c = m.group(1).upper()
            if mapping.pop(c, None) is None:
                print(f"  There was no substitution for {c}.")
            else:
                print(f"  Substitution for {c} removed.")
            continue

        # Add a substitution: v=e, v->e, v:e, ve
        m = re.fullmatch(r"([a-z])(?:=|->|:)?([a-z])", token)
        if m:
            c, p = m.group(1).upper(), m.group(2)
            if c not in CIPHER:
                print(f"  Letter {c} is not in the ciphertext, skipping.")
                continue
            # If this plain letter is already used by another cipher letter, reassign it
            for old_c, old_p in list(mapping.items()):
                if old_p == p and old_c != c:
                    del mapping[old_c]
                    print(f"  Letter {p} was previously used for {old_c}; substitution for {old_c} removed.")
            mapping[c] = p
            continue

        print(f"  Did not understand '{token}'. Format: v=e (type help for help).")
    return True


def interactive_decrypt():
    mapping = {}
    print("CIPHERTEXT (UPPERCASE):\n")
    print(CIPHER)
    print(HELP)

    while True:
        try:
            cmd = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not process_command(cmd, mapping):
            break

        print("\n" + apply_mapping(CIPHER, mapping))
        show_mapping(mapping)

    result = apply_mapping(CIPHER, mapping)
    with open("decrypted.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("\nFinal text saved to decrypted.txt")
    print("Substitutions:", ", ".join(f"{c}->{p}" for c, p in sorted(mapping.items())) or "none")


if __name__ == "__main__":
    # Optionally pass a file path to decrypt a different text.
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            CIPHER = f.read().upper()

    interactive_decrypt()